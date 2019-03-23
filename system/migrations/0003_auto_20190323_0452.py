# Generated by Django 3.0 on 2019-03-23 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system', '0002_auto_20190319_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='componenet',
            name='course',
        ),
        migrations.RemoveField(
            model_name='componenet',
            name='module',
        ),
        migrations.DeleteModel(
            name='Component_in_Module',
        ),
        migrations.RemoveField(
            model_name='componentimage',
            name='componenet_ptr',
        ),
        migrations.RemoveField(
            model_name='componenttext',
            name='componenet_ptr',
        ),
        migrations.RemoveField(
            model_name='course',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='module',
            name='course',
        ),
        migrations.RemoveField(
            model_name='question',
            name='module',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='course',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='module',
        ),
        migrations.RemoveField(
            model_name='take',
            name='course',
        ),
        migrations.RemoveField(
            model_name='take',
            name='learner',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='username',
        ),
        migrations.RemoveField(
            model_name='learner',
            name='email',
        ),
        migrations.RemoveField(
            model_name='learner',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='learner',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='learner',
            name='username',
        ),
        migrations.AddField(
            model_name='instructor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='learner',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Componenet',
        ),
        migrations.DeleteModel(
            name='ComponentImage',
        ),
        migrations.DeleteModel(
            name='ComponentText',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Module',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='Take',
        ),
    ]
