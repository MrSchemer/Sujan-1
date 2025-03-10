# Generated by Django 5.1.6 on 2025-02-25 05:30

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_blog_contact_honor_organization_involved_publication_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='honor',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='organization_involved',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='publication',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='research',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
