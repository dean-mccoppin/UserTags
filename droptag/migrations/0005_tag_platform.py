# Generated by Django 3.0.8 on 2021-01-06 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('droptag', '0004_auto_20210105_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='platform',
            field=models.CharField(choices=[('PSN', 'PlayStation Network ID'), ('XB', 'Xbox Gamertag'), ('DC', 'Discord Username'), ('STM', 'Steam Username')], default='STM', max_length=32),
        ),
    ]
