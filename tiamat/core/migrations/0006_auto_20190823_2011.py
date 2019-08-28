# Generated by Django 2.2.3 on 2019-08-23 20:11

from django.db import migrations, models
import django.db.models.deletion
import tiamat.core.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190821_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorypage',
            name='body',
            field=wagtail.core.fields.StreamField([('theme_header', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('text', wagtail.core.blocks.TextBlock())])), ('feature_slider', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('features', wagtail.core.blocks.ListBlock(tiamat.core.blocks.FeatureBlock))])), ('text_feature_row', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('paragraphs', wagtail.core.blocks.ListBlock(tiamat.core.blocks.TextParagraphBlock))])), ('center_image_feature', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('emphasis_title', wagtail.core.blocks.CharBlock(classname='title', icon='title', required=False)), ('subtitle', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('features_left', wagtail.core.blocks.ListBlock(tiamat.core.blocks.IconTextParagraphBlock)), ('features_right', wagtail.core.blocks.ListBlock(tiamat.core.blocks.IconTextParagraphBlock))])), ('stacked_feature_list', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('subtitle', wagtail.core.blocks.CharBlock(classname='title', icon='title', required=False)), ('features', wagtail.core.blocks.ListBlock(tiamat.core.blocks.StackedFeatureBlock))])), ('highlight_text', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('text', wagtail.core.blocks.TextBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('column', wagtail.core.blocks.StructBlock([('columns', wagtail.core.blocks.IntegerBlock()), ('content', wagtail.core.blocks.StreamBlock([('h2', wagtail.core.blocks.StructBlock([('show_line', wagtail.core.blocks.BooleanBlock(required=False)), ('tag', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title'))])), ('tagged_h2', wagtail.core.blocks.StructBlock([('tag', wagtail.core.blocks.CharBlock()), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title'))])), ('line_h2', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='title', icon='title'))])), ('rich_text', wagtail.core.blocks.RichTextBlock()), ('action_button', wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.TextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_url', wagtail.core.blocks.URLBlock())]))]))])), ('wide_image', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('author', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('subtitle', wagtail.core.blocks.CharBlock()), ('portrait', wagtail.images.blocks.ImageChooserBlock(required=False)), ('first_name', wagtail.core.blocks.CharBlock()), ('last_name', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.TextBlock())])), ('author_quote', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('quote', wagtail.core.blocks.TextBlock()), ('portrait', wagtail.images.blocks.ImageChooserBlock(required=False)), ('first_name', wagtail.core.blocks.CharBlock()), ('last_name', wagtail.core.blocks.CharBlock())])), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='code', label='Raw HTML'))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='body',
            field=wagtail.core.fields.StreamField([('theme_header', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('text', wagtail.core.blocks.TextBlock())])), ('feature_slider', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('features', wagtail.core.blocks.ListBlock(tiamat.core.blocks.FeatureBlock))])), ('text_feature_row', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('paragraphs', wagtail.core.blocks.ListBlock(tiamat.core.blocks.TextParagraphBlock))])), ('center_image_feature', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('emphasis_title', wagtail.core.blocks.CharBlock(classname='title', icon='title', required=False)), ('subtitle', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('features_left', wagtail.core.blocks.ListBlock(tiamat.core.blocks.IconTextParagraphBlock)), ('features_right', wagtail.core.blocks.ListBlock(tiamat.core.blocks.IconTextParagraphBlock))])), ('stacked_feature_list', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('subtitle', wagtail.core.blocks.CharBlock(classname='title', icon='title', required=False)), ('features', wagtail.core.blocks.ListBlock(tiamat.core.blocks.StackedFeatureBlock))])), ('highlight_text', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('text', wagtail.core.blocks.TextBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('column', wagtail.core.blocks.StructBlock([('columns', wagtail.core.blocks.IntegerBlock()), ('content', wagtail.core.blocks.StreamBlock([('h2', wagtail.core.blocks.StructBlock([('show_line', wagtail.core.blocks.BooleanBlock(required=False)), ('tag', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title'))])), ('tagged_h2', wagtail.core.blocks.StructBlock([('tag', wagtail.core.blocks.CharBlock()), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title'))])), ('line_h2', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='title', icon='title'))])), ('rich_text', wagtail.core.blocks.RichTextBlock()), ('action_button', wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.TextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_url', wagtail.core.blocks.URLBlock())]))]))])), ('wide_image', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('author', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('subtitle', wagtail.core.blocks.CharBlock()), ('portrait', wagtail.images.blocks.ImageChooserBlock(required=False)), ('first_name', wagtail.core.blocks.CharBlock()), ('last_name', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.TextBlock())])), ('author_quote', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('quote', wagtail.core.blocks.TextBlock()), ('portrait', wagtail.images.blocks.ImageChooserBlock(required=False)), ('first_name', wagtail.core.blocks.CharBlock()), ('last_name', wagtail.core.blocks.CharBlock())])), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='code', label='Raw HTML'))], blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.CoreImage')),
            ],
        ),
        migrations.AddField(
            model_name='landingpage',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Author'),
        ),
    ]
