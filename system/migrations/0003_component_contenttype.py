# Generated by Django 2.1.7 on 2019-03-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20190325_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='contentType',
            field=models.IntegerField(choices=[(0, 'text'), (1, 'image')], default=0),
            preserve_default=False,
        ),
    ]
