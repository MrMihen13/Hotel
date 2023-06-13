# Generated by Django 4.2.2 on 2023-06-13 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("guest", "0002_alter_guest_options"),
        ("room", "0003_alter_room_bathroom_type_alter_room_room_class"),
        ("booking", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="booking",
            options={"verbose_name": "Бронь", "verbose_name_plural": "Брони"},
        ),
        migrations.AlterField(
            model_name="booking",
            name="guest",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="guest.guest",
                verbose_name="Постоялец",
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="number",
            field=models.CharField(
                editable=False, max_length=8, verbose_name="Код бронирования"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="booking",
            unique_together={("room", "date_start", "date_end")},
        ),
    ]
