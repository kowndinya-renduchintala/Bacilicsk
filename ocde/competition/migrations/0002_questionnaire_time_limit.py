# Generated by Django 3.1.2 on 2020-11-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='time_limit',
            field=models.IntegerField(default=1),
        ),
    ]
