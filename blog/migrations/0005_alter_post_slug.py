# Generated by Django 3.2 on 2021-04-24 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_auto_20210424_2015"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(default="", max_length=200, unique=True),
        ),
    ]