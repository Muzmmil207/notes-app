# Generated by Django 4.1.3 on 2023-02-02 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="remind",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Reminder"),
        ),
    ]
