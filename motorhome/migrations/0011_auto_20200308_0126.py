# Generated by Django 2.2.5 on 2020-03-07 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motorhome', '0010_auto_20200308_0121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='pub_date',
            new_name='event_date',
        ),
    ]
