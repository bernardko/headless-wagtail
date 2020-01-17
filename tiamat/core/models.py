from django import forms
from django.db import models
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, render_to_response, redirect

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel,
                                         MultiFieldPanel, PageChooserPanel,
                                         StreamFieldPanel)
from wagtail.admin.utils import send_mail
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.blocks import PageChooserBlock, StreamBlock, StructBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Orderable, Page, Site
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import AbstractImage, AbstractRendition, Image
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from headlesspreview.models import HeadlessPreviewMixin

from .blocks import LandingBlock, StoryBlock

@register_snippet
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ForeignKey(
        'core.CoreImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    intro = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.full_name

    def __unicode__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    panels = [
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        ImageChooserPanel('image'),
        FieldPanel('intro'),
        FieldPanel('description'),
    ]

# A couple of abstract classes that contain commonly used fields

class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

    class Meta:
        abstract = True


class ContactFields(models.Model):
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    post_code = models.CharField(max_length=10, blank=True)

    panels = [
        FieldPanel('telephone'),
        FieldPanel('email'),
        FieldPanel('address_1'),
        FieldPanel('address_2'),
        FieldPanel('city'),
        FieldPanel('country'),
        FieldPanel('post_code'),
    ]

    class Meta:
        abstract = True



# Custom image
class CoreImage(AbstractImage):
    credit = models.CharField(max_length=255, blank=True)

    admin_form_fields = Image.admin_form_fields + (
        'credit',
    )

    @property
    def credit_text(self):
        return self.credit


class CoreRendition(AbstractRendition):
    image = models.ForeignKey('CoreImage', on_delete=models.CASCADE, related_name='renditions')

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )

class NavMenu(Orderable):
    landing_page = ParentalKey('core.LandingPage', related_name="navmenu_set")
    name = models.CharField(max_length=255)
    section_id = models.CharField(max_length=50, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    @property
    def get_link(self):
        if self.link_page:
            return self.link_page.url
        else:
            return self.link

    panels = [
        FieldPanel('name'),
        FieldPanel('section_id'),
        FieldPanel('link_page'),
        FieldPanel('link'),
    ]

class BasePage(Page):
    menu_title = models.CharField(max_length=255)
    intro = models.TextField(blank=True)

    class Meta:
        abstract = True

class LandingPage(HeadlessPreviewMixin, BasePage):
    feed_image = models.ForeignKey(
        'core.CoreImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL)
    body = StreamField(LandingBlock(required=False), null=True, blank=True)

    def get_sitemap_urls(self):
        site = self.get_site()
        return [{
            'location':'https://%s%s' % (site.hostname, self.url),
            "lastmod":(self.last_published_at or self.latest_revision_created_at),
            "changefreq":"monthly",
            "priority":1
        }]


LandingPage.content_panels = [
    FieldPanel('title', classname="full"),
    FieldPanel('menu_title'),
    ImageChooserPanel('feed_image'),
    FieldPanel('intro'),
    FieldPanel('author'),
    InlinePanel('navmenu_set'),
    StreamFieldPanel('body'),
]

class CategoryPage(HeadlessPreviewMixin, BasePage):
    body = StreamField(LandingBlock(required=False), null=True, blank=True)
    num_per_page = models.IntegerField(default=10)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
    ]

    @property
    def landing_pages(self):
        return  LandingPage.objects.live().descendant_of(self).order_by('-date')

    def serve(self, request):
        return render(request, self.template, {
            'self': self,
            'landing_pages': self.landing_pages,
            'num_per_page': self.num_per_page,
        })

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('menu_title'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        FieldPanel('num_per_page')
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]