# Generated by Django 5.0.1 on 2024-02-27 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_meduim_link_profilemodel_medium_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]