# Generated by Django 3.1.5 on 2021-01-23 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210123_0746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farm',
            old_name='farm',
            new_name='owner',
        ),
    ]
