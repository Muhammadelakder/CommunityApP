# Generated by Django 3.2.6 on 2021-12-17 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0005_alter_store_id'),
        ('wishlists', '0003_rename_stores_wishlist_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('ACCEPTED', 'ACCEPTED'), ('FULFILLED', 'FULFILLED')], default='PENDING', max_length=10),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wishlists', to='stores.store'),
        ),
    ]
