# Generated by Django 3.2.6 on 2021-12-17 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0002_rename_wishmaker_wishlist_wishmaster'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='stores',
            new_name='store',
        ),
    ]