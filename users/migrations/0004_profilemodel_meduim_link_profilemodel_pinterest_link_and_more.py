# Generated by Django 5.0.1 on 2024-02-21 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profilemodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='meduim_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='pinterest_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='profile_bio',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='quora_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='reddit_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='website_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
