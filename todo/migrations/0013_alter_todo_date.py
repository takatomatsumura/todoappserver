# Generated by Django 3.2.6 on 2021-09-07 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_auto_20210907_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(default='2021-09-07 16:47'),
        ),
    ]
