# Generated by Django 2.2.1 on 2019-08-14 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.IntegerField(),
        ),
    ]