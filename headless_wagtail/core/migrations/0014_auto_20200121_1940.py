# Generated by Django 2.2.3 on 2020-01-21 19:40

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('core', '0013_auto_20200121_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='pagefiltertag',
            name='category_tag',
        ),
        migrations.AddField(
            model_name='pagefiltertag',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='taggit.Tag'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='core.LandingPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='CategoryTag',
        ),
        migrations.AddField(
            model_name='landingpagetag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='core.LandingPage'),
        ),
        migrations.AddField(
            model_name='landingpagetag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='core_landingpagetag_items', to='taggit.Tag'),
        ),
    ]
