# Generated by Django 5.0.3 on 2024-04-03 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_apl_n'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('name', models.CharField(max_length=256)),
                ('games', models.IntegerField()),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='APL',
        ),
    ]
