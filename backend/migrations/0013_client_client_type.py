# Generated by Django 5.0.7 on 2024-09-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_type',
            field=models.CharField(blank=True, choices=[('fizicko lice', 'Fizicko lice'), ('agencija', 'Agencija'), ('investitor', 'Investitor'), ('banka', 'Banka'), ('drugo pravno lice', 'Drugo pravno lice')], max_length=32),
        ),
    ]
