# Generated by Django 3.2.6 on 2021-12-11 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_auto_20211211_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
