# Generated by Django 4.2.1 on 2023-06-30 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_order_shoppingcart_orderitem"),
    ]

    operations = [
        migrations.AddField(
            model_name="regulardelivery",
            name="delivery_cycle",
            field=models.IntegerField(default=0),
        ),
    ]
