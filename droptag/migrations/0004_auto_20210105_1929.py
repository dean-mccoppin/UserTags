# Generated by Django 3.0.8 on 2021-01-06 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('droptag', '0003_auto_20201231_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tag',
            name='time_met',
            field=models.DateField(),
        ),
    ]
