# Generated by Django 3.2.4 on 2021-10-24 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineOrder', '0003_auto_20211024_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlineorders',
            name='ordered_products',
        ),
        migrations.AddField(
            model_name='onlineorders',
            name='products_selection',
            field=models.ManyToManyField(related_name='_OnlineOrder_onlineorders_products_selection_+', to='OnlineOrder.OnlineOrders'),
        ),
    ]