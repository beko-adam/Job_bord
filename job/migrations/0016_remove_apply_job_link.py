# Generated by Django 2.2.12 on 2021-09-01 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_auto_20210901_0850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='job_link',
        ),
    ]
