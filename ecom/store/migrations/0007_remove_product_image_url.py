# Generated by Django 4.2.11 on 2024-04-12 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0006_product_image_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="image_url",
        ),
    ]
