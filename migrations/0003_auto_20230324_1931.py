# Generated by Django 3.2.18 on 2023-03-24 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0002_auto_20230324_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='account',
            name='gift_balance',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
