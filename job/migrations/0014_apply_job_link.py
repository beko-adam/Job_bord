# Generated by Django 2.2.12 on 2021-08-30 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_remove_apply_job_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='job_link',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.Job', verbose_name='apply_jop'),
            preserve_default=False,
        ),
    ]
