# Generated by Django 3.2.4 on 2021-10-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineOrder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('ordered_products', models.CharField(max_length=500)),
            ],
        ),
    ]
