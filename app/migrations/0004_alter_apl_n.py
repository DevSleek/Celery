# Generated by Django 5.0.3 on 2024-04-02 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_place_apl_games_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apl',
            name='n',
            field=models.IntegerField(null=True),
        ),
    ]