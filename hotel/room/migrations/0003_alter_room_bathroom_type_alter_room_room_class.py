# Generated by Django 4.2.2 on 2023-06-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("room", "0002_alter_room_options_room_place_count_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="bathroom_type",
            field=models.CharField(
                choices=[("Совмещенный", "Combined"), ("Раздельный", "Separate")],
                default="Совмещенный",
                max_length=12,
                verbose_name="Тип санузла",
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="room_class",
            field=models.CharField(
                choices=[
                    ("Эконом", "Economy"),
                    ("Стандарт", "Standard"),
                    ("Стандарт улучшенный", "Standard Superior"),
                    ("Полулюкс", "Junior Suite"),
                    ("Люкс", "Luxury"),
                ],
                default="Эконом",
                max_length=20,
                verbose_name="Класс номера",
            ),
        ),
    ]
