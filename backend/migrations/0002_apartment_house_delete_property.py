# Generated by Django 5.0.7 on 2024-08-07 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('variety', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('listing_type', models.CharField(choices=[('prodaja', 'Prodaja'), ('iznajmljivanje', 'Iznajmljivanje')], max_length=20)),
                ('area', models.DecimalField(decimal_places=2, max_digits=7)),
                ('rooms', models.IntegerField()),
                ('heating', models.CharField(max_length=50)),
                ('floor', models.IntegerField()),
                ('furnishing', models.CharField(max_length=50)),
                ('additional_furnishing', models.TextField(blank=True, null=True)),
                ('structure', models.CharField(choices=[('garsonjera', 'Garsonjera'), ('jednosoban stan', 'Jednosoban Stan'), ('dvosoban stan', 'dvosoban stan')], max_length=23)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('variety', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('listing_type', models.CharField(choices=[('prodaja', 'Prodaja'), ('iznajmljivanje', 'Iznajmljivanje')], max_length=20)),
                ('area', models.DecimalField(decimal_places=2, max_digits=7)),
                ('rooms', models.IntegerField()),
                ('heating', models.CharField(max_length=50)),
                ('floor', models.IntegerField()),
                ('furnishing', models.CharField(max_length=50)),
                ('additional_furnishing', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]
