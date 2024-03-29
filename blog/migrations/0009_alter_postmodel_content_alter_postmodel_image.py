# Generated by Django 5.0.1 on 2024-02-21 20:53

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_postmodel_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(blank=True, default='thumbnail1.png', null=True, upload_to='uploads/'),
        ),
    ]
