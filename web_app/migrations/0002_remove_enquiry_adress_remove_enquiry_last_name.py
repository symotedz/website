# Generated by Django 4.2.1 on 2023-09-08 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='Adress',
        ),
        migrations.RemoveField(
            model_name='enquiry',
            name='last_name',
        ),
    ]