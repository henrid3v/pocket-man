# Generated by Django 4.0 on 2022-03-13 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20201203_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='is_gain',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='is_spent',
        ),
        migrations.AddField(
            model_name='activity',
            name='type',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]