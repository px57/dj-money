# Generated by Django 4.2 on 2023-09-25 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activated', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text="The object's creation date/time", null=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now_add=True, help_text="The object's last update date/time", null=True, verbose_name='updated on')),
                ('balance', models.PositiveBigIntegerField(default=0)),
                ('gift_balance', models.PositiveBigIntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='profiles.profile', unique=True)),
            ],
            options={
                'verbose_name': 'Compte',
                'verbose_name_plural': 'Comptes',
            },
        ),
        migrations.CreateModel(
            name='TransfertModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activated', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text="The object's creation date/time", null=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now_add=True, help_text="The object's last update date/time", null=True, verbose_name='updated on')),
                ('accounting_type', models.CharField(choices=[('debit', 'debit'), ('credit', 'credit')], max_length=255)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('gift_amount', models.PositiveIntegerField(default=0)),
                ('type', models.CharField(choices=[('playroom_playdraw', 'playroom_playdraw'), ('playroom_win', 'playroom_win'), ('deposit', 'deposit'), ('withdraw', 'withdraw'), ('transfer', 'transfer'), ('bonus', 'bonus')], max_length=255)),
                ('destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='money.account')),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source', to='money.account')),
            ],
            options={
                'verbose_name': 'Transfert',
                'verbose_name_plural': 'Transferts',
            },
        ),
    ]
