# Generated by Django 4.2.9 on 2024-01-04 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Workout",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Set",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("reps", models.IntegerField()),
                ("weight", models.IntegerField()),
                ("date", models.DateField()),
                ("workout", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="fitness.workout")),
            ],
        ),
        migrations.CreateModel(
            name="Exercise",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("sets", models.ManyToManyField(to="fitness.set")),
            ],
        ),
    ]
