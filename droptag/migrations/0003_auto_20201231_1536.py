# Generated by Django 3.0.8 on 2020-12-31 20:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('droptag', '0002_tag_date_filed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='date_filed',
        ),
        migrations.AddField(
            model_name='tag',
            name='date_filled',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]