# Generated by Django 3.1.6 on 2021-04-06 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_admin_addinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_addinfo',
            name='fees',
            field=models.IntegerField(null=True),
        ),
    ]
