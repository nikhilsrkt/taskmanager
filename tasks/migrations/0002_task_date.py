# Generated by Django 5.1 on 2024-08-16 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
