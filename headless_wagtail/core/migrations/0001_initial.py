# Generated by Django 2.2.3 on 2019-07-29 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import taggit.managers
import headless_wagtail.core.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.core.models
import wagtail.images.blocks
import wagtail.images.models
import wagtail.search.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('file', models.ImageField(height_field='height', upload_to=wagtail.images.models.get_upload_to, verbose_name='file', width_field='width')),
                ('width', models.IntegerField(editable=False, verbose_name='width')),
                ('height', models.IntegerField(editable=False, verbose_name='height')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('focal_point_x', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_y', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_width', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_height', models.PositiveIntegerField(blank=True, null=True)),
                ('file_size', models.PositiveIntegerField(editable=False, null=True)),
                ('file_hash', models.CharField(blank=True, editable=False, max_length=40)),
                ('credit', models.CharField(blank=True, max_length=255)),
                ('collection', models.ForeignKey(default=wagtail.core.models.get_root_collection_id, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Collection', verbose_name='collection')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text=None, through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags')),
                ('uploaded_by_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='uploaded by user')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField([('feature_slider', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('features', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.FeatureBlock))])), ('text_feature_row', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('paragraphs', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.TextParagraphBlock))])), ('center_image_feature', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('emphasis_title', wagtail.core.blocks.CharBlock(classname='title', icon='title', required=False)), ('subtitle', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('features_left', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.IconTextParagraphBlock)), ('features_right', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.IconTextParagraphBlock))])), ('stacked_feature_list', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('subtitle', wagtail.core.blocks.CharBlock(classname='title', icon='title', required=False)), ('features', wagtail.core.blocks.ListBlock(headless_wagtail.core.blocks.StackedFeatureBlock))])), ('highlight_text', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(required=False)), ('section_classes', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('text', wagtail.core.blocks.TextBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='code', label='Raw HTML')), ('article_section', wagtail.core.blocks.StreamBlock([('tagged_h2', wagtail.core.blocks.StructBlock([])), ('line_h2', wagtail.core.blocks.StructBlock([])), ('rich_text', wagtail.core.blocks.StructBlock([])), ('author', wagtail.core.blocks.StructBlock([])), ('author_quote', wagtail.core.blocks.StructBlock([])), ('action_button', wagtail.core.blocks.StructBlock([]))]))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='NavMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=255)),
                ('section_id', models.CharField(blank=True, max_length=50, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('landing_page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='navmenu_set', to='core.LandingPage')),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CoreRendition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_spec', models.CharField(db_index=True, max_length=255)),
                ('file', models.ImageField(height_field='height', upload_to=wagtail.images.models.get_rendition_upload_to, width_field='width')),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
                ('focal_point_key', models.CharField(blank=True, default='', editable=False, max_length=16)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='renditions', to='core.CoreImage')),
            ],
            options={
                'unique_together': {('image', 'filter_spec', 'focal_point_key')},
            },
        ),
    ]
