# Generated by Django 5.1.6 on 2025-02-26 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_honor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='honor',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
