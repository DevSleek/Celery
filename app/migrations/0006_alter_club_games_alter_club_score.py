# Generated by Django 5.0.3 on 2024-04-03 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_club_delete_apl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='games',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='club',
            name='score',
            field=models.CharField(max_length=256),
        ),
    ]