# Generated by Django 4.1 on 2022-09-05 05:56

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currencysymbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('currency', models.CharField(max_length=50)),
                ('currency_symbol', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
