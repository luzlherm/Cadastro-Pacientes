# Generated by Django 5.0.6 on 2024-07-29 14:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("agendamentos", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="agendamentos",
            old_name="obs",
            new_name="observação",
        ),
    ]
