# Generated by Django 5.0 on 2023-12-06 16:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0002_alter_cartitem_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="price",
            field=models.DecimalField(decimal_places=5, max_digits=8),
        ),
    ]