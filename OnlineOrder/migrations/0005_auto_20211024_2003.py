# Generated by Django 3.2.4 on 2021-10-24 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineOrder', '0004_auto_20211024_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlineorders',
            name='products_selection',
        ),
        migrations.AddField(
            model_name='onlineorders',
            name='products_selection',
            field=models.CharField(default=123, max_length=500),
            preserve_default=False,
        ),
    ]
