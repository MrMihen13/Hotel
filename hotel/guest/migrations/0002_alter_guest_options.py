# Generated by Django 4.2.2 on 2023-06-13 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("guest", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="guest",
            options={"verbose_name": "Постоялец", "verbose_name_plural": "Постояльцы"},
        ),
    ]
