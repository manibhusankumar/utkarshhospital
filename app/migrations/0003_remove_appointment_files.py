# Generated by Django 3.1.6 on 2021-04-03 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210404_0337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='files',
        ),
    ]