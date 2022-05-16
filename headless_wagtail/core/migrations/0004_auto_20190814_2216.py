# Generated by Django 2.2.3 on 2019-08-14 22:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import headlesspreview.models
import headless_wagtail.core.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('core', '0003_auto_20190803_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', models.TextField(blank=True)),
                ('body', wagtail.core.fields.StreamField([('feature_slider', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('features', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.FeatureBlock))])), ('text_feature_row', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('paragraphs', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.TextParagraphBlock))])), ('center_image_feature', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('emphasis_title', wagtail.core.blocks.CharBlock(classname='title', icon='title', required=False)), ('subtitle', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('features_left', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.IconTextParagraphBlock)), ('features_right', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.IconTextParagraphBlock))])), ('stacked_feature_list', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('subtitle', wagtail.core.blocks.CharBlock(classname='title', icon='title', required=False)), ('features', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.StackedFeatureBlock))])), ('highlight_text', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('text', wagtail.core.blocks.TextBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('column', wagtail.core.blocks.StructBlock([('columns', wagtail.core.blocks.IntegerBlock()), ('content', wagtail.core.blocks.StreamBlock([('tagged_h2', wagtail.core.blocks.StructBlock([('tag', wagtail.core.blocks.CharBlock()), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title'))])), ('line_h2', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='title', icon='title'))])), ('rich_text', wagtail.core.blocks.RichTextBlock()), ('action_button', wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.TextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_url', wagtail.core.blocks.URLBlock())]))]))])), ('author', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('subtitle', wagtail.core.blocks.CharBlock()), ('portrait', wagtail.images.blocks.ImageChooserBlock(required=False)), ('first_name', wagtail.core.blocks.CharBlock()), ('last_name', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.TextBlock())])), ('author_quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock()), ('portrait', wagtail.images.blocks.ImageChooserBlock(required=False)), ('first_name', wagtail.core.blocks.CharBlock()), ('last_name', wagtail.core.blocks.CharBlock())])), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='code', label='Raw HTML'))], blank=True, null=True)),
                ('num_per_page', models.IntegerField(default=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(headlesspreview.models.HeadlessPreviewMixin, 'wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='landingpage',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='landingpage',
            name='intro',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='body',
            field=wagtail.core.fields.StreamField([('feature_slider', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('features', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.FeatureBlock))])), ('text_feature_row', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('paragraphs', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.TextParagraphBlock))])), ('center_image_feature', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('emphasis_title', wagtail.core.blocks.CharBlock(classname='title', icon='title', required=False)), ('subtitle', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('features_left', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.IconTextParagraphBlock)), ('features_right', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.IconTextParagraphBlock))])), ('stacked_feature_list', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('subtitle', wagtail.core.blocks.CharBlock(classname='title', icon='title', required=False)), ('features', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.StackedFeatureBlock))])), ('highlight_text', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('text', wagtail.core.blocks.TextBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('column', wagtail.core.blocks.StructBlock([('columns', wagtail.core.blocks.IntegerBlock()), ('content', wagtail.core.blocks.StreamBlock([('tagged_h2', wagtail.core.blocks.StructBlock([('tag', wagtail.core.blocks.CharBlock()), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title'))])), ('line_h2', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='title', icon='title'))])), ('rich_text', wagtail.core.blocks.RichTextBlock()), ('action_button', wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.TextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_url', wagtail.core.blocks.URLBlock())]))]))])), ('author', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('subtitle', wagtail.core.blocks.CharBlock()), ('portrait', wagtail.images.blocks.ImageChooserBlock(required=False)), ('first_name', wagtail.core.blocks.CharBlock()), ('last_name', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.TextBlock())])), ('author_quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock()), ('portrait', wagtail.images.blocks.ImageChooserBlock(required=False)), ('first_name', wagtail.core.blocks.CharBlock()), ('last_name', wagtail.core.blocks.CharBlock())])), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='code', label='Raw HTML'))], blank=True, null=True),
        ),
    ]
