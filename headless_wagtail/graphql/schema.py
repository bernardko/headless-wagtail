# Borrowed from wagtail-torchbox
import json
import graphene

from collections import namedtuple

from django.conf import settings
from graphene.types import Scalar
from graphql.validation.rules import NoUnusedFragments, specified_rules
from graphene_django.converter import convert_django_field
from graphene_django import DjangoObjectType
from wagtail.contrib.redirects.models import Redirect
from wagtail.core.models import Page
from wagtail_graphql.types.streamfield import convert_stream_field
from wagtail.contrib.redirects.models import Redirect

from .streamfield import DefaultStreamBlock, create_stream_field_type
from .utils import serialize_rich_text

from headless_wagtail.core.models import CoreImage, LandingPage, CategoryPage

specified_rules[:] = [
    rule for rule in specified_rules
    if rule is not NoUnusedFragments
]

def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())

def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

@convert_django_field.register(CoreImage)
def convert_image(field, registry=None):
    return WagtailImageNode(
        description=field.help_text, required=not field.null
    )

class WagtailImageRendition(graphene.ObjectType):
    id = graphene.ID()
    url = graphene.String()
    width = graphene.Int()
    height = graphene.Int()


class WagtailImageRenditionList(graphene.ObjectType):
    rendition_list = graphene.List(WagtailImageRendition)
    src_set = graphene.String()

    def resolve_src_set(self, info):
        return ", ".join(
            [f"{img.url} {img.width}w" for img in self.rendition_list])


class WagtailImageNode(DjangoObjectType):
    class Meta:
        model = CoreImage
        #exclude_fields = ['tags']
    
    #Define all available image rendition options as arguments
    rendition = graphene.Field(
        WagtailImageRendition,
        max=graphene.String(),
        min=graphene.String(),
        width=graphene.Int(),
        height=graphene.Int(),
        fill=graphene.String(),
        format=graphene.String(),
        bgcolor=graphene.String(),
        jpegquality=graphene.Int()
    )
    rendition_list = graphene.Field(
        WagtailImageRenditionList, sizes=graphene.List(graphene.Int))

    def resolve_rendition(self, info, **kwargs):
        filters = "|".join([f"{key}-{val}" for key, val in kwargs.items()])
        img = self.get_rendition(filters)
        return WagtailImageRendition(
            id=img.id, url=img.url, width=img.width, height=img.height)

    def resolve_rendition_list(self, info, sizes=[]):
        rendition_list = [
            WagtailImageNode.resolve_rendition(self, info, width=width)
            for width in sizes
        ]
        return WagtailImageRenditionList(rendition_list=rendition_list)

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
    credit = graphene.String()

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
    first_published_at = graphene.types.datetime.DateTime()
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

class ImageTypeBlock(DefaultStreamBlock):
    image = graphene.Field(ImageObjectType)

    def resolve_image(self, info):
        try:
            return CoreImage.objects.get(id=self.image)
        except CoreImage.DoesNotExist:
            return None

class WideImageBlock(ImageTypeBlock):
    pass

class FeatureSliderBlock(DefaultStreamBlock):
    features = graphene.List(ImageTypeBlock)

    def resolve_features(self, info, **kwargs):
        features = []
        for feature in self.features:
            features.append(ImageTypeBlock(image=feature['image']))
        return features

class StackedFeatureListBlock(DefaultStreamBlock):
    features = graphene.List(ImageTypeBlock)

    def resolve_features(self, info, **kwargs):
        features = []
        for feature in self.features:
            features.append(ImageTypeBlock(image=feature['image']))
        return features

class AuthorBlock(DefaultStreamBlock):
    portrait = graphene.Field(ImageObjectType)

    def resolve_portrait(self, info):
        try:
            return CoreImage.objects.get(id=self.portrait)
        except CoreImage.DoesNotExist:
            return None

class IconTextParagraphBlock(ImageTypeBlock):
    pass

class TextImageBlock(ImageTypeBlock):
    pass

class WagtailPageType(DefaultStreamBlock):
    search_image = graphene.Field(ImageObjectType)

    class Meta:
        interfaces = [PageInterface]

class RelatedLinkBlock(DefaultStreamBlock):
    page = graphene.Field(WagtailPageType)

    def resolve_page(self, info, **kwargs):
        return Page.objects.get(id=self.page).specific

class RelatedLinksBlock(DefaultStreamBlock):
    (links, resolve_links) = create_stream_field_type('links', **{"links": RelatedLinkBlock})

column_field_handlers = {
    "text_image": TextImageBlock,
    "related_links": RelatedLinksBlock,
}

class CenterImageFeatureBlock(ImageTypeBlock):
    (features_left, resolve_features_left) = create_stream_field_type('features_left', **{"features_left": IconTextParagraphBlock})
    (features_right, resolve_features_right) = create_stream_field_type('features_right', **{"features_right": IconTextParagraphBlock})

class ColumnBlock(DefaultStreamBlock):
    (content, resolve_content) = create_stream_field_type('content', **column_field_handlers)

stream_field_handers = {
    "wide_image": WideImageBlock, 
    "feature_slider": FeatureSliderBlock, 
    "center_image_feature": CenterImageFeatureBlock, 
    "stacked_feature_list": StackedFeatureListBlock,
    "author": AuthorBlock,
    "column": ColumnBlock
}

class StreamField(Scalar):
    @staticmethod
    def serialize(val):
        return val
        #return StreamFieldSerialiser().serialise_stream_block(val)

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


class LandingPageObjectType(DjangoObjectType):
    intro = graphene.String()
    author = graphene.Field(AuthorObjectType)
    breadcrumbs = graphene.List(BreadcrumbObjectType)
    #body = graphene.List(StreamField)
    (body, resolve_body) = create_stream_field_type('body', **stream_field_handers)

    class Meta:
        model = LandingPage
        interfaces = [PageInterface]

    def resolve_author(self, info, **kwargs):
        return self.author

    def resolve_breadcrumbs(self, info, **kwargs):
        return self.get_ancestors()[1:]

    # def resolve_body(self, info, **kwargs):
    #     stream_block_object_type, graphql_block_dict = StreamFieldBuilder().build_stream_block(self.body)

    #     field = graphene.List(stream_block_object_type)
    #     LandingPageObjectType._meta.fields.update({'body': field})
    #     setattr(LandingPageObjectType, 'body', field)

    #     blocks = StreamFieldSerialiser().serialise_stream_block(self.body)
    #     #blocks_tuple = json2obj(json.dumps(blocks))
    #     graphql_blocks = []
    #     for block in blocks:
    #         block_node_cls = graphql_block_dict[block['type']]
    #         block_node = block_node_cls(**block['value'])
    #         graphql_blocks.append(block_node)
    
    #     return graphql_blocks

class CategoryPageObjectType(graphene.ObjectType):
    intro = graphene.String()
    breadcrumbs = graphene.List(BreadcrumbObjectType)
    #body = StreamField()
    (body, resolve_body) = create_stream_field_type('body', **stream_field_handers)
    num_per_page = graphene.Int()
    landing_pages = graphene.List(LandingPageObjectType, search=graphene.String(), first=graphene.Int(),skip=graphene.Int())

    def resolve_breadcrumbs(self, info, **kwargs):
        return self.get_ancestors()[1:]

    def resolve_landing_pages(self, info, search=None, first=None, skip=None, **kwargs):
        qs = self.landing_pages.in_site(info.context.site)

        if search:
            filter = (
                Q(title__icontains=search) |
                Q(intro__icontains=search)
            )
            qs = qs.filter(filter)

        qs = qs.order_by('-last_published_at')

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
    children = graphene.List('headless_wagtail.graphql.schema.NavMenuItemObjectType')

    def resolve_name(self, info, **kwargs):
        return self.specific.menu_title

    def resolve_link_url(self, info, **kwargs):
        return self.get_url(current_site=info.context.site)

    def resolve_children(self, info, **kwargs):
        nav_menu_items = Page.objects.in_site(info.context.site).live().public().in_menu().descendant_of(self)

        return nav_menu_items

class RedirectObjectType(DjangoObjectType):
    old_path = graphene.String()
    link = graphene.String()

    class Meta:
        model = Redirect

    def resolve_old_path(self, info, **kwargs):
        return self.old_path

    def resolve_link(self, info, **kwargs):
        if self.redirect_page:
            return self.redirect_page.get_url(current_site=info.context.site)
        elif self.redirect_link:
            return self.redirect_link

def get_page_preview(model, token):
    return model.get_page_from_preview_token(token)

class Query(graphene.ObjectType):
    nav_menu_items = graphene.List(NavMenuItemObjectType)
    landing_pages = graphene.List(LandingPageObjectType, preview_token=graphene.String(), slug=graphene.String())
    category_pages = graphene.List(CategoryPageObjectType, preview_token=graphene.String(), slug=graphene.String())
    images = graphene.List(ImageObjectType, ids=graphene.List(graphene.Int))
    redirects = graphene.List(RedirectObjectType)

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

    def resolve_redirects(self, info, **kwargs):
        redirects = Redirect.objects.filter(site=info.context.site).all()
        
        return redirects

schema = graphene.Schema(
    query=Query,
)