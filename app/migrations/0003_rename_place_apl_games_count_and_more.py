# Generated by Django 5.0.3 on 2024-04-02 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_apl_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apl',
            old_name='place',
            new_name='games_count',
        ),
        migrations.RenameField(
            model_name='apl',
            old_name='score',
            new_name='score_count',
        ),
    ]
