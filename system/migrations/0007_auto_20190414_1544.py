# Generated by Django 3.0 on 2019-04-14 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_auto_20190403_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='finish_time',
            field=models.DateField(default=None, null=True),
        ),
    ]