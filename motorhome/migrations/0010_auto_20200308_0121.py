# Generated by Django 2.2.5 on 2020-03-07 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorhome', '0009_auto_20200308_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Дата та час події'),
        ),
    ]
