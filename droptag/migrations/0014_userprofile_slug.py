# Generated by Django 3.0.8 on 2021-01-26 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('droptag', '0013_auto_20210126_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(default=383726, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
