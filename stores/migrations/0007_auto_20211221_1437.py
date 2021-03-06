# Generated by Django 3.2.10 on 2021-12-21 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0006_alter_store_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='address',
            field=models.CharField(max_length=65),
        ),
        migrations.AlterField(
            model_name='store',
            name='city',
            field=models.CharField(max_length=65),
        ),
        migrations.AlterField(
            model_name='store',
            name='id',
            field=models.CharField(max_length=65, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=65),
        ),
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.CharField(max_length=65, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_type',
            field=models.CharField(max_length=65, null=True),
        ),
    ]
