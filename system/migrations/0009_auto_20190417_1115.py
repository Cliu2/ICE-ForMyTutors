# Generated by Django 2.1.7 on 2019-04-17 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0008_auto_20190417_1056'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Token',
            new_name='MyToken',
        ),
    ]
