# Generated by Django 3.1.7 on 2021-04-08 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20210408_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
    ]