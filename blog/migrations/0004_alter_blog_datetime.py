# Generated by Django 4.0.1 on 2022-01-11 05:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 11, 11, 12, 5, 608733)),
        ),
    ]