# Generated by Django 3.1.5 on 2021-02-11 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20210211_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='samplingpoint',
            name='clinicalAnalysi',
        ),
        migrations.AddField(
            model_name='clinicalanalysis',
            name='samplingPoint',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.samplingpoint'),
        ),
    ]
