# Generated by Django 4.2.1 on 2023-05-06 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
    ]
