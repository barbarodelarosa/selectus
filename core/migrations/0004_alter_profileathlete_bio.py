# Generated by Django 4.0.6 on 2022-08-01 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profileathlete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileathlete',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
