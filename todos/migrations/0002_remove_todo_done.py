# Generated by Django 3.1 on 2020-09-05 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='done',
        ),
    ]
