# Generated by Django 4.1 on 2022-08-18 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_completed',
            field=models.BooleanField(default=True),
        ),
    ]