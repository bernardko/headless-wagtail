# Generated by Django 2.2.3 on 2020-01-17 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('core', '0011_auto_20200117_0044'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RedirectLink',
        ),
    ]