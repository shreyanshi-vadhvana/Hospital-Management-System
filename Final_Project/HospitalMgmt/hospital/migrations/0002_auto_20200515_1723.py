# Generated by Django 3.0.6 on 2020-05-15 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='total_days',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='total_days',
        ),
    ]
