# Generated by Django 3.1.4 on 2021-01-06 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210106_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='participants',
            field=models.ManyToManyField(related_name='team', to='app.Students', verbose_name='Участники'),
        ),
        migrations.DeleteModel(
            name='StudentsInTeams',
        ),
    ]