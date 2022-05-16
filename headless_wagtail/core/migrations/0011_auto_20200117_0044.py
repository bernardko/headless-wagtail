# Generated by Django 2.2.3 on 2020-01-17 00:44

from django.db import migrations, models
import django.db.models.deletion
import headless_wagtail.core.blocks
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtaildocs', '0010_document_file_hash'),
        ('core', '0010_auto_20190901_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorypage',
            name='body',
            field=wagtail.core.fields.StreamField([('theme_header', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('text', wagtail.core.blocks.TextBlock())])), ('default_header', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('tag', wagtail.core.blocks.CharBlock(required=False))])), ('feature_slider', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('features', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.FeatureBlock))])), ('text_feature_row', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('paragraphs', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.TextParagraphBlock))])), ('center_image_feature', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('emphasis_title', wagtail.core.blocks.CharBlock(classname='title', icon='title', required=False)), ('emphasis', wagtail.core.blocks.BooleanBlock(required=False)), ('subtitle', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('features_left', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.IconTextParagraphBlock)), ('features_right', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.IconTextParagraphBlock))])), ('stacked_feature_list', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('subtitle', wagtail.core.blocks.CharBlock(classname='title', icon='title', required=False)), ('features', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.StackedFeatureBlock))])), ('highlight_text', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('text', wagtail.core.blocks.TextBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(required=False)), ('button_url', wagtail.core.blocks.CharBlock(required=False))])), ('column', wagtail.core.blocks.StructBlock([('columns', wagtail.core.blocks.IntegerBlock()), ('content', wagtail.core.blocks.StreamBlock([('h2', wagtail.core.blocks.StructBlock([('align_center', wagtail.core.blocks.BooleanBlock(required=False)), ('show_line', wagtail.core.blocks.BooleanBlock(required=False)), ('tag', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon', wagtail.core.blocks.CharBlock(required=False)), ('emoji', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('emphasis', wagtail.core.blocks.BooleanBlock(required=False))])), ('tagged_h2', wagtail.core.blocks.StructBlock([('tag', wagtail.core.blocks.CharBlock()), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title'))])), ('line_h2', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='title', icon='title'))])), ('rich_text', wagtail.core.blocks.RichTextBlock()), ('action_button', wagtail.core.blocks.StructBlock([('align_center', wagtail.core.blocks.BooleanBlock(required=False)), ('description', wagtail.core.blocks.TextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_url', wagtail.core.blocks.CharBlock())])), ('text_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_col_size', wagtail.core.blocks.IntegerBlock(default=4)), ('align_image_left', wagtail.core.blocks.BooleanBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock())])), ('summary', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock())])), ('related_links', wagtail.core.blocks.StructBlock([('links', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.RelatedLinkBlock))])), ('table', wagtail.contrib.table_block.blocks.TableBlock())]))])), ('wide_image', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('author', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('subtitle', wagtail.core.blocks.CharBlock()), ('portrait', wagtail.images.blocks.ImageChooserBlock(required=False)), ('first_name', wagtail.core.blocks.CharBlock()), ('last_name', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.TextBlock())])), ('author_quote', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('quote', wagtail.core.blocks.TextBlock()), ('portrait', wagtail.images.blocks.ImageChooserBlock(required=False)), ('first_name', wagtail.core.blocks.CharBlock()), ('last_name', wagtail.core.blocks.CharBlock())])), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='code', label='Raw HTML'))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='body',
            field=wagtail.core.fields.StreamField([('theme_header', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('text', wagtail.core.blocks.TextBlock())])), ('default_header', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('tag', wagtail.core.blocks.CharBlock(required=False))])), ('feature_slider', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('features', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.FeatureBlock))])), ('text_feature_row', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('paragraphs', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.TextParagraphBlock))])), ('center_image_feature', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('emphasis_title', wagtail.core.blocks.CharBlock(classname='title', icon='title', required=False)), ('emphasis', wagtail.core.blocks.BooleanBlock(required=False)), ('subtitle', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('features_left', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.IconTextParagraphBlock)), ('features_right', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.IconTextParagraphBlock))])), ('stacked_feature_list', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('subtitle', wagtail.core.blocks.CharBlock(classname='title', icon='title', required=False)), ('features', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.StackedFeatureBlock))])), ('highlight_text', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('text', wagtail.core.blocks.TextBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(required=False)), ('button_url', wagtail.core.blocks.CharBlock(required=False))])), ('column', wagtail.core.blocks.StructBlock([('columns', wagtail.core.blocks.IntegerBlock()), ('content', wagtail.core.blocks.StreamBlock([('h2', wagtail.core.blocks.StructBlock([('align_center', wagtail.core.blocks.BooleanBlock(required=False)), ('show_line', wagtail.core.blocks.BooleanBlock(required=False)), ('tag', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon', wagtail.core.blocks.CharBlock(required=False)), ('emoji', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('emphasis', wagtail.core.blocks.BooleanBlock(required=False))])), ('tagged_h2', wagtail.core.blocks.StructBlock([('tag', wagtail.core.blocks.CharBlock()), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title'))])), ('line_h2', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='title', icon='title'))])), ('rich_text', wagtail.core.blocks.RichTextBlock()), ('action_button', wagtail.core.blocks.StructBlock([('align_center', wagtail.core.blocks.BooleanBlock(required=False)), ('description', wagtail.core.blocks.TextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_url', wagtail.core.blocks.CharBlock())])), ('text_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_col_size', wagtail.core.blocks.IntegerBlock(default=4)), ('align_image_left', wagtail.core.blocks.BooleanBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock())])), ('summary', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock())])), ('related_links', wagtail.core.blocks.StructBlock([('links', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.RelatedLinkBlock))])), ('table', wagtail.contrib.table_block.blocks.TableBlock())]))])), ('wide_image', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('author', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('subtitle', wagtail.core.blocks.CharBlock()), ('portrait', wagtail.images.blocks.ImageChooserBlock(required=False)), ('first_name', wagtail.core.blocks.CharBlock()), ('last_name', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.TextBlock())])), ('author_quote', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('quote', wagtail.core.blocks.TextBlock()), ('portrait', wagtail.images.blocks.ImageChooserBlock(required=False)), ('first_name', wagtail.core.blocks.CharBlock()), ('last_name', wagtail.core.blocks.CharBlock())])), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='code', label='Raw HTML'))], blank=True, null=True),
        ),
        migrations.CreateModel(
            name='RedirectLink',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('link_external', models.URLField(blank=True, verbose_name='External link')),
                ('menu_title', models.CharField(max_length=255)),
                ('link_document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]