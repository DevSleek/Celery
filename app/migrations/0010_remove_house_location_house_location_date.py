# Generated by Django 5.0.3 on 2024-04-04 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_house_delete_club'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='location',
        ),
        migrations.AddField(
            model_name='house',
            name='location_date',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
