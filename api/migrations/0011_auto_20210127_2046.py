# Generated by Django 3.1.5 on 2021-01-27 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_planting_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planting',
            name='activities',
        ),
        migrations.RemoveField(
            model_name='planting',
            name='collections',
        ),
        migrations.AddField(
            model_name='samplingpoint',
            name='planting',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.planting'),
        ),
    ]
