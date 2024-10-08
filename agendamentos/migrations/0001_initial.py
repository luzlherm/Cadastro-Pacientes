# Generated by Django 5.0.6 on 2024-07-23 18:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("pacientes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Agendamentos",
            fields=[
                ("id_agendamento", models.AutoField(primary_key=True, serialize=False)),
                ("data_hora", models.DateTimeField()),
                ("data_criacao", models.DateTimeField(auto_now_add=True)),
                ("cancelado", models.BooleanField(default=False)),
                ("obs", models.TextField(blank=True, null=True)),
                ("tipo", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "id_paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="agendamentos",
                        to="pacientes.pacientes",
                    ),
                ),
            ],
            options={
                "db_table": "agendamentos",
                "managed": True,
            },
        ),
    ]
