# Generated by Django 3.2.7 on 2021-09-23 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_courses_sessionyearmodel_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='session_year_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.sessionyearmodel'),
        ),
    ]