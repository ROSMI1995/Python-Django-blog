# Generated by Django 4.0.4 on 2022-06-08 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_post_header_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='header_image',
            new_name='image',
        ),
    ]
