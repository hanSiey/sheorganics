# Generated by Django 3.2.4 on 2021-10-25 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineOrder', '0006_auto_20211025_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlineorders',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]
