# Borrowed from wagtail-torchbox

from django.conf import settings

import graphene
from graphene.types import Scalar
from graphql.validation.rules import NoUnusedFragments, specified_rules
from wagtail.contrib.redirects.models import Redirect
from wagtail.core.models import Page

from .streamfield import StreamFieldSerialiser
from .utils import serialize_rich_text

from tiamat.core.models import CoreImage, LandingPage, CategoryPage

specified_rules[:] = [
    rule for rule in specified_rules
    if rule is not NoUnusedFragments
]

class RichTextString(Scalar):
    @staticmethod
    def serialize(value):
        return serialize_rich_text(value)

class ImageRenditionObjectType(graphene.ObjectType):
    url = graphene.String()
    width = graphene.Int()
    height = graphene.Int()
    hash = graphene.String()

    def resolve_url(self, info):
        return settings.MEDIA_PREFIX + self.file.url

    def resolve_hash(self, format):
        return self.image.get_file_hash()


class ImageObjectType(graphene.ObjectType):
    FORMATS = {
        'quarter': 'width-400',  # Used by aligned image when alignment is either "left" or "right"
        'half': 'width-800',  # Used by aligned image when alignment is "half"
        'full': 'width-1280',
        'max': 'width-1920',
        'logo': 'max-250x80',  # Used by logo block
        'icon': 'fill-100x100',
        'large-icon': 'fill-400x400',
        # Search images
        'facebook': 'width-1024',
        'twitter': 'width-400',
    }

    id = graphene.Int()
    src = graphene.String()
    alt = graphene.String()
    hash = graphene.String()
    rendition = graphene.Field(ImageRenditionObjectType, format=graphene.String())
    width = graphene.Int()
    height = graphene.Int()

    def resolve_alt(self, info):
        return self.title

    def resolve_src(self, info):
        return settings.MEDIA_PREFIX + self.file.url

    def resolve_hash(self, info):
        return self.get_file_hash()

    def resolve_rendition(self, info, format):
        if format in ImageObjectType.FORMATS:
            return self.get_rendition(ImageObjectType.FORMATS[format])

        # TODO: Error

class PageInterface(graphene.Interface):
    title = graphene.String()
    page_title = graphene.String()
    last_published_at = graphene.types.datetime.DateTime()
    search_description = graphene.String()
    search_image = graphene.Field(ImageObjectType)
    slug = graphene.String()
    specific_page_type = graphene.String()
    page_url = graphene.String()

    def resolve_page_title(self, info):
        title = ''
        if self.seo_title:
            title += self.seo_title
        else:
            title += self.title

        return title

    def resolve_search_description(self, info):
        description = self.title

        if hasattr(self, 'listing_summary'):
            if self.listing_summary:
                description = self.listing_summary

        if hasattr(self, 'search_description'):
            if self.search_description:
                description = self.search_description

        return description

    def resolve_search_image(self, info, **kwargs):
        if hasattr(self, 'feed_image') and self.feed_image:
            return self.feed_image

    def resolve_specific_page_type(self, info):
        return '%s.%s' % (self._meta.app_label, self.specific.__class__.__name__)

    def resolve_page_url(self, info):
        return self.get_url(current_site=info.context.site)

class StreamField(Scalar):
    @staticmethod
    def serialize(val):
        return StreamFieldSerialiser().serialise_stream_block(val)

class AuthorObjectType(graphene.ObjectType):
    full_name = graphene.String()
    image = graphene.Field(ImageObjectType)
    intro = graphene.String()
    description = graphene.String()

class BreadcrumbObjectType(graphene.ObjectType):
    menu_title = graphene.String()
    link_url = graphene.String()

    def resolve_menu_title(self, info, **kwargs):
        return self.specific.menu_title

    def resolve_link_url(self, info, **kwargs):
        return self.get_url(current_site=info.context.site)

class LandingPageObjectType(graphene.ObjectType):
    intro = graphene.String()
    author = graphene.Field(AuthorObjectType)
    breadcrumbs = graphene.List(BreadcrumbObjectType)
    body = StreamField()
    
    class Meta:
        interfaces = [PageInterface]
        
    def resolve_author(self, info, **kwargs):
        return self.author

    def resolve_breadcrumbs(self, info, **kwargs):
        return self.get_ancestors()[1:]

class CategoryPageObjectType(graphene.ObjectType):
    intro = graphene.String()
    breadcrumbs = graphene.List(BreadcrumbObjectType)
    body = StreamField()
    num_per_page = graphene.Int()
    landing_pages = graphene.List(LandingPageObjectType, search=graphene.String(), first=graphene.Int(),skip=graphene.Int())

    def resolve_breadcrumbs(self, info, **kwargs):
        return self.get_ancestors()[1:]

    def resolve_landing_pages(self, info, search=None, first=None, skip=None, **kwargs):
        qs = LandingPage.objects.in_site(info.context.site).live().public().descendant_of(self)

        if search:
            filter = (
                Q(title__icontains=search) |
                Q(intro__icontains=search)
            )
            qs = qs.filter(filter)

        qs = qs.order_by('-first_published_at')

        if skip:
            qs = qs[skip:]

        if first:
            qs = qs[:first]

        return qs

    class Meta:
        interfaces = [PageInterface]

class NavMenuItemObjectType(graphene.ObjectType):
    name = graphene.String()
    link_url = graphene.String()
    children = graphene.List('tiamat.graphql.schema.NavMenuItemObjectType')

    def resolve_name(self, info, **kwargs):
        return self.specific.menu_title

    def resolve_link_url(self, info, **kwargs):
        return self.get_url(current_site=info.context.site)

    def resolve_children(self, info, **kwargs):
        nav_menu_items = Page.objects.in_site(info.context.site).live().public().in_menu().descendant_of(self)

        return nav_menu_items

def get_page_preview(model, token):
    return model.get_page_from_preview_token(token)

class Query(graphene.ObjectType):
    nav_menu_items = graphene.List(NavMenuItemObjectType)
    landing_pages = graphene.List(LandingPageObjectType, preview_token=graphene.String(), slug=graphene.String())
    category_pages = graphene.List(CategoryPageObjectType, preview_token=graphene.String(), slug=graphene.String())
    images = graphene.List(ImageObjectType, ids=graphene.List(graphene.Int))

    def resolve_nav_menu_items(self, info, **kwargs):
        nav_menu_items = Page.objects.in_site(info.context.site).live().public().in_menu()

        return nav_menu_items

    def resolve_landing_pages(self, info, **kwargs):
        landing_pages = LandingPage.objects.in_site(info.context.site).live().public().order_by('title')

        if 'preview_token' in kwargs:
            page = get_page_preview(LandingPage, kwargs['preview_token'])
            if page:
                return [page]
            else:
                return []

        if 'slug' in kwargs:
            landing_pages = landing_pages.filter(slug=kwargs['slug'])

        return landing_pages

    def resolve_category_pages(self, info, **kwargs):
        category_pages = CategoryPage.objects.in_site(info.context.site).live().public().order_by('title')

        if 'preview_token' in kwargs:
            page = get_page_preview(CategoryPage, kwargs['preview_token'])
            if page:
                return [page]
            else:
                return []

        if 'slug' in kwargs:
            category_pages = category_pages.filter(slug=kwargs['slug'])

        return category_pages

    def resolve_images(self, info, **kwargs):
        images = CoreImage.objects.all()
        if 'ids' in kwargs:
            images = images.filter(id__in=kwargs['ids'])

        return images

schema = graphene.Schema(
    query=Query,
)