# Generated by Django 4.2.2 on 2023-06-10 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("room", "0001_initial"),
        ("guest", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_start", models.DateField(verbose_name="Дата начала")),
                ("date_end", models.DateField(verbose_name="Дата конца")),
                ("number", models.IntegerField(verbose_name="Код бронирования")),
                (
                    "guest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="guest.guest",
                        verbose_name="Постоялец",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="room.room",
                        verbose_name="Номер",
                    ),
                ),
            ],
        ),
    ]