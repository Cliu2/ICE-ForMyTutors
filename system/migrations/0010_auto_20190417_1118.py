# Generated by Django 2.1.7 on 2019-04-17 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0009_auto_20190417_1115'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyToken',
            new_name='Token',
        ),
    ]
