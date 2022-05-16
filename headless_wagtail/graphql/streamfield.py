# Borrowed from wagtail-torchbox

import wagtail
import graphene
import string 

from django.conf import settings

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.images.models import Image
from wagtail.embeds.blocks import EmbedBlock
from wagtail.embeds.embeds import get_embed
from wagtail.embeds.exceptions import EmbedException
from wagtail.images.blocks import ImageChooserBlock

from .utils import serialize_rich_text

from graphene.types.generic import GenericScalar

# We're creating a fallback / default ObjectType at this point
class DefaultStreamBlock(graphene.ObjectType):
    block_type = graphene.String()
    value = GenericScalar()

# This is our factory function
# Pass in kwargs with the block's name as the 
# keyword and the graphene type as its value
StreamFieldTypes = {}
def create_stream_field_type(field_name, **kwargs):
    block_type_handlers = kwargs.copy()

    class Meta:
        types = (DefaultStreamBlock, ) + tuple(
            block_type_handlers.values())
    
    # This is where we generate the UnionType from the kwargs
    # Different graphene types can't have the same name, so we're
    # generating this class dynamically
    type_name = f"{string.capwords(field_name, sep='_').replace('_', '')}Type"
    if type_name not in StreamFieldTypes:
        StreamFieldType = type(
            f"{string.capwords(field_name, sep='_').replace('_', '')}Type",
            (graphene.Union,),
            dict(Meta=Meta))
        StreamFieldTypes[type_name] = StreamFieldType
    else:
        StreamFieldType = StreamFieldTypes[type_name]

    def convert_block(block):
        block_type = block.get('type')
        # When block is not a stream block
        if not block_type:
            block_type = list(block_type_handlers.keys())[0]
            block = {"type":block_type, "value":block}

        value = block.get('value')

        if block_type in block_type_handlers:
            handler = block_type_handlers.get(block_type)
            if isinstance(value, dict):
                # Reconstruct value to pass only existing fields from handler
                existing_key_dict = {}
                for key, field in handler._meta.fields.items():
                    if key in value:
                        existing_key_dict[key] = value[key]
                return handler(value=value, block_type=block_type, **existing_key_dict)
            else:
                return handler(value=value, block_type=block_type)
        else:
            return DefaultStreamBlock(value=value, block_type=block_type)

    # We also generate the resolver function for the field
    def resolve_field(self, info):
        field = getattr(self, field_name)
        if hasattr(field, "stream_data"):
            return [convert_block(block) for block in field.stream_data]
        elif isinstance(field, list):
            block_list = []
            for block in field:
                block_list.append(convert_block(block))
            return block_list
        else:
            raise Exception("Invalid Field Data resolve_field:" + str(field))

    return (graphene.List(StreamFieldType), resolve_field)

# graphene_block_map = {
#     # choosers
#     #wagtail.images.blocks.ImageChooserBlock: (Image, _resolve_image),
#     #wagtail.core.blocks.PageChooserBlock: (Page, _resolve_page),
#     #wagtail.snippets.blocks.SnippetChooserBlock: (_snippet_handler, _resolve_snippet),
#     # standard fields
#     wagtail.core.blocks.CharBlock.__class__.__name__: graphene.types.String,
#     wagtail.core.blocks.URLBlock.__class__.__name__: graphene.types.String,
#     wagtail.core.blocks.DateBlock.__class__.__name__: graphene.types.Date,
#     wagtail.core.blocks.DateTimeBlock.__class__.__name__: graphene.types.DateTime,
#     wagtail.core.blocks.BooleanBlock.__class__.__name__: graphene.types.Boolean,
#     wagtail.core.blocks.IntegerBlock.__class__.__name__: graphene.types.Int,
#     wagtail.core.blocks.FloatBlock.__class__.__name__: graphene.types.Float,
#     wagtail.core.blocks.DecimalBlock.__class__.__name__: graphene.types.String,
#     wagtail.core.blocks.TextBlock.__class__.__name__: graphene.types.String,
#     wagtail.core.blocks.TimeBlock.__class__.__name__: graphene.types.Time,
#     wagtail.core.blocks.RichTextBlock.__class__.__name__: graphene.types.String,
#     wagtail.core.blocks.RawHTMLBlock.__class__.__name__: graphene.types.String,
#     wagtail.core.blocks.BlockQuoteBlock.__class__.__name__: graphene.types.String,
#     wagtail.core.blocks.ChoiceBlock.__class__.__name__: graphene.types.String,
#     wagtail.core.blocks.RegexBlock.__class__.__name__: graphene.types.String,
#     wagtail.core.blocks.EmailBlock.__class__.__name__: graphene.types.String,
#     wagtail.core.blocks.StaticBlock.__class__.__name__: graphene.types.String,
# }

# class Block(graphene.ObjectType):
#     pass

# class StreamFieldBuilder:

#     def build_struct_block(self, block, value):
#         struct_block_object_type = Block
#         for field_name, value in value.items():
#             child_block = block.child_blocks[field_name]

#             block_object = self.build_block(child_block, value)
#             field = graphene.Field(block_object)
#             struct_block_object_type._meta.fields.update({field_name: field})
#             setattr(struct_block_object_type, field_name, field)

#         return struct_block_object_type

#     def build_list_block(self, block, value):
#         for child_value in value:
#             block_object = self.build_block(block.child_block, child_value)
#             break

#         list_block_object_type = graphene.List(block_object)

#         return list_block_object_type

#     def build_stream_block(self, value):
#         stream_block_object_type = Block

#         blocks = {}
#         for child_block in value:
#             block_object = self.build_block(child_block.block, child_block.value)
#             blocks[child_block.block_type] = block_object
#             field = graphene.Field(block_object)
#             stream_block_object_type._meta.fields.update({child_block.block_type: field})
#             setattr(stream_block_object_type, child_block.block_type, field)

#         return (stream_block_object_type, blocks,)

#     def build_block(self, block, value):
#         if hasattr(block, 'to_graphql_representation'):
#             return block.to_graphql_representation(value)
#         elif isinstance(block, blocks.RichTextBlock):
#             return graphene.String
#         elif isinstance(block, EmbedBlock):
#             pass
#         elif isinstance(block, ImageChooserBlock):
#             pass
#         elif isinstance(block, blocks.StructBlock):
#             return self.build_struct_block(block, value)
#         elif isinstance(block, blocks.ListBlock):
#             return self.build_list_block(block, value)
#         elif isinstance(block, blocks.StreamBlock):
#             return self.build_stream_block(value)
#         else:
#             return graphene_block_map.get(block.__class__.__name__)

# class StreamFieldSerialiser:
#     def serialise_struct_block(self, block, value):
#         blocks = {}
#         for field_name, value in value.items():
#             child_block = block.child_blocks[field_name]
#             blocks[field_name] = self.serialise_block(child_block, value)

#         return blocks

#     def serialise_list_block(self, block, value):
#         blocks = []
#         for child_value in value:
#             blocks.append(self.serialise_block(block.child_block, child_value))

#         return blocks

#     def serialise_stream_block(self, value):
#         blocks = []
#         for child_block in value:
#             blocks.append({
#                 'type': child_block.block_type,
#                 'value': self.serialise_block(child_block.block, child_block.value),
#             })

#         return blocks

#     def serialise_block(self, block, value):
#         if hasattr(block, 'to_graphql_representation'):
#             return block.to_graphql_representation(value)
#         elif isinstance(block, blocks.RichTextBlock):
#             return serialize_rich_text(value.source)
#         elif isinstance(block, EmbedBlock):
#             try:
#                 embed = get_embed(value.url)
#                 return {
#                     'html': embed.html,
#                     'url': value.url,
#                 }
#             except EmbedException:
#                 return {
#                     'html': '',
#                     'url': None
#                 }
#         elif isinstance(block, ImageChooserBlock):
#             # FIXME
#             if value is None:
#                 return None
                
#             return {
#                 'id': value.id,
#                 'alt': value.title,
#                 'src': settings.MEDIA_PREFIX + value.file.url,
#                 'credit': value.credit,
#                 'hash': value.get_file_hash()
#             }
            
#         elif isinstance(block, blocks.FieldBlock):
#             return value
#         elif isinstance(block, blocks.StructBlock):
#             return self.serialise_struct_block(block, value)
#         elif isinstance(block, blocks.ListBlock):
#             return self.serialise_list_block(block, value)
#         elif isinstance(block, blocks.StreamBlock):
#             return self.serialise_stream_block(value)