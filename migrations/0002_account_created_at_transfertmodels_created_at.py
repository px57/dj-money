# Generated by Django 4.2 on 2024-02-20 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text="The object's creation date/time", null=True, verbose_name='created at'),
        ),
        migrations.AddField(
            model_name='transfertmodels',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text="The object's creation date/time", null=True, verbose_name='created at'),
        ),
    ]
