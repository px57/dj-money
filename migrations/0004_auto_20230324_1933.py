# Generated by Django 3.2.18 on 2023-03-24 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20230311_1213'),
        ('money', '0003_auto_20230324_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='profiles.profile', unique=True),
        ),
        migrations.AlterField(
            model_name='transfertmodels',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transfertmodels',
            name='gift_amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
