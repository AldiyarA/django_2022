# Generated by Django 2.2.27 on 2022-04-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220426_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
