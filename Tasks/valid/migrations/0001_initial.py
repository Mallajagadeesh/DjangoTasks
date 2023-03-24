# Generated by Django 4.1 on 2022-09-05 05:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datamodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=60, validators=[django.core.validators.RegexValidator(message='password must be contain 8 letters and a capital letter and a special character', regex='^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$')])),
                ('gender', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
