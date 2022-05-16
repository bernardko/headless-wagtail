from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtail.core.blocks import (CharBlock, FieldBlock, ListBlock,
                                 BooleanBlock, TextBlock, URLBlock,
                                 ChoiceBlock, EmailBlock, IntegerBlock,
                                 RawHTMLBlock, RichTextBlock, StreamBlock,
                                 StructBlock, PageChooserBlock)
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('left', 'Wrap left'),
        ('right', 'Wrap right'),
        ('half', 'Half width'),
        ('full', 'Full width'),
    ))


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    alignment = ImageFormatChoiceBlock()
    caption = CharBlock()
    attribution = CharBlock(required=False)

    class Meta:
        icon = "image"


class PhotoGridBlock(StructBlock):
    images = ListBlock(ImageChooserBlock())

    class Meta:
        icon = "grip"


class PullQuoteBlock(StructBlock):
    quote = CharBlock(classname="quote title")
    attribution = CharBlock()

    class Meta:
        icon = "openquote"


class PullQuoteImageBlock(StructBlock):
    quote = CharBlock()
    attribution = CharBlock()
    image = ImageChooserBlock(required=False)


class BustoutBlock(StructBlock):
    image = ImageChooserBlock()
    text = RichTextBlock()

    class Meta:
        icon = "pick"


class WideImage(StructBlock):
    image = ImageChooserBlock()

    class Meta:
        icon = "image"


class StatsBlock(StructBlock):
    pass

    class Meta:
        icon = "order"

class StoryBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title")
    h3 = CharBlock(icon="title", classname="title")
    h4 = CharBlock(icon="title", classname="title")
    intro = RichTextBlock(icon="pilcrow")
    paragraph = RichTextBlock(icon="pilcrow")
    aligned_image = ImageBlock(label="Aligned image")
    wide_image = WideImage(label="Wide image")
    bustout = BustoutBlock()
    pullquote = PullQuoteBlock()
    raw_html = RawHTMLBlock(label='Raw HTML', icon="code")
    embed = EmbedBlock(icon="code")

class BaseBlock(StructBlock):
    section_id = CharBlock(required=False)
    section_classes = CharBlock(required=False)

class FeatureBlock(StructBlock):
    title = TextBlock(required=True)
    subtitle = CharBlock(icon="title", classname="title", required=False)
    show_action_button = BooleanBlock(required=False)
    button_text = CharBlock(required=False)
    button_url = URLBlock(required=False)
    caption_text = CharBlock(required=False)
    caption_link = URLBlock(required=False)
    image = ImageChooserBlock(required=False)
    image_position = CharBlock(required=False, default="center center / cover no-repeat")
    overlay_image = ImageChooserBlock(required=False)
    overlay_position_top = CharBlock(required=False)
    overlay_position_right = CharBlock(required=False)

class FeatureSliderBlock(BaseBlock):
    features = ListBlock(FeatureBlock)

class TextParagraphBlock(StructBlock):
    title = CharBlock(icon="title", classname="title")
    text = TextBlock()
    link_text = CharBlock(required=False)
    link_url = URLBlock(required=False)

class TextFeatureRowBlock(BaseBlock):
    paragraphs = ListBlock(TextParagraphBlock)

class IconTextParagraphBlock(StructBlock):
    title = CharBlock(icon="title", classname="title")
    icon = CharBlock(required=False)
    image = ImageChooserBlock(required=False)
    text = TextBlock()

class CenterImageFeatureBlock(BaseBlock):
    title = CharBlock(icon="title", classname="title")
    emphasis_title = CharBlock(required=False, icon="title", classname="title")
    emphasis = BooleanBlock(required=False)
    subtitle = CharBlock(icon="title", classname="title")
    image = ImageChooserBlock(required=False)

    features_left = ListBlock(IconTextParagraphBlock)
    features_right = ListBlock(IconTextParagraphBlock)

class StackedFeatureBlock(BaseBlock):
    highlight_tag = CharBlock(required=False)
    title = CharBlock(icon="title", classname="title")
    text = TextBlock()
    image = ImageChooserBlock(required=False)
    link_text = CharBlock(required=False)
    link_url = URLBlock(required=False)

class StackedFeatureListBlock(BaseBlock):
    title = CharBlock(icon="title", classname="title")
    subtitle = CharBlock(icon="title", classname="title", required=False)
    features = ListBlock(StackedFeatureBlock)

class HighlightTextBlock(BaseBlock):
    fa_icon = CharBlock(required=False)
    image = ImageChooserBlock(required=False)
    title = CharBlock(icon="title", classname="title")
    text = TextBlock(required=False)
    button_text = CharBlock(required=False)
    button_url = CharBlock(required=False)

class AuthorBlock(BaseBlock):
    title = CharBlock(icon="title", classname="title")
    subtitle = CharBlock()
    portrait = ImageChooserBlock(required=False)
    first_name = CharBlock()
    last_name = CharBlock()
    description = TextBlock()

class AuthorQuoteBlock(BaseBlock):
    quote = TextBlock()
    portrait = ImageChooserBlock(required=False)
    first_name = CharBlock()
    last_name = CharBlock()

class WideImageBlock(BaseBlock):
    image = ImageChooserBlock(required=False)

class ThemeHeaderBlock(BaseBlock):
    title = CharBlock(icon="title", classname="title")
    text = TextBlock()

class DefaultHeaderBlock(BaseBlock):
    tag = CharBlock(required=False)

# Column Blocks

class TaggedH2Block(StructBlock):
    tag = CharBlock()
    title = CharBlock(icon="title", classname="title")

class LineH2Block(StructBlock):
    title = CharBlock(icon="title", classname="title")

class H2Block(StructBlock):
    align_center = BooleanBlock(required=False)
    show_line = BooleanBlock(required=False)
    tag = CharBlock(required=False)
    fa_icon = CharBlock(required=False)
    emoji = CharBlock(required=False)
    title = CharBlock(icon="title", classname="title")
    emphasis = BooleanBlock(required=False)

class ActionButtonBlock(StructBlock):
    align_center = BooleanBlock(required=False)
    description = TextBlock()
    button_text = CharBlock()
    button_url = CharBlock()

class TextImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    image_col_size = IntegerBlock(default=4)
    align_image_left = BooleanBlock(required=False)
    text = RichTextBlock()

class SummaryBlock(StructBlock):
    text = RichTextBlock()

class RelatedLinkBlock(StructBlock):
    page = PageChooserBlock()
    
    title = CharBlock(required=False)
    page_url = CharBlock(required=False)
    search_description = TextBlock(required=False)

class RelatedLinksBlock(StructBlock):
    links = ListBlock(RelatedLinkBlock)

class ColumnContentBlock(StreamBlock):
    h2 = H2Block()
    tagged_h2 = TaggedH2Block()
    line_h2 = LineH2Block()
    rich_text = RichTextBlock()
    action_button = ActionButtonBlock()
    text_image = TextImageBlock()
    summary = SummaryBlock()
    related_links = RelatedLinksBlock()
    table = TableBlock()

class ColumnBlock(StructBlock):
    columns = IntegerBlock()
    content = ColumnContentBlock()

class LandingBlock(StreamBlock):
    theme_header = ThemeHeaderBlock()
    default_header = DefaultHeaderBlock()
    feature_slider = FeatureSliderBlock()
    text_feature_row = TextFeatureRowBlock()
    center_image_feature = CenterImageFeatureBlock()
    stacked_feature_list = StackedFeatureListBlock()
    highlight_text = HighlightTextBlock()
    column = ColumnBlock()
    wide_image = WideImageBlock()
    author = AuthorBlock()
    author_quote = AuthorQuoteBlock()
    raw_html = RawHTMLBlock(label='Raw HTML', icon="code")
    