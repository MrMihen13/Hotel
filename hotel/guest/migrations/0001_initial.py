# Generated by Django 4.2.2 on 2023-06-10 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("room", "0001_initial"),
        ("hotel", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Guest",
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
                ("name", models.CharField(max_length=128, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=128, verbose_name="Фамилия")),
                (
                    "middle_name",
                    models.CharField(max_length=123, verbose_name="Отчество"),
                ),
                (
                    "passport_series",
                    models.DecimalField(
                        decimal_places=0, max_digits=6, verbose_name="Серия паспорта"
                    ),
                ),
                (
                    "passport_number",
                    models.DecimalField(
                        decimal_places=0, max_digits=6, verbose_name="Номер паспорта"
                    ),
                ),
                (
                    "passport_date_issue",
                    models.DateField(verbose_name="Дата выдачи паспорта"),
                ),
                (
                    "passport_place_issue",
                    models.TextField(verbose_name="Место выдачи паспорта"),
                ),
                ("arrival_date", models.DateField(verbose_name="Дата приезда")),
                ("departure_date", models.DateField(verbose_name="Дата отъезда")),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hotel.country",
                        verbose_name="Страна",
                    ),
                ),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hotel.hotel",
                        verbose_name="Отель",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="room.room",
                        verbose_name="Номер в отеле",
                    ),
                ),
            ],
        ),
    ]