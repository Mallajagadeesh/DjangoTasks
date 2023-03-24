# Generated by Django 4.1 on 2022-09-05 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='barcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=500)),
                ('product_code', models.CharField(max_length=50)),
                ('pack_code', models.CharField(max_length=400)),
                ('br_code', models.BinaryField(max_length=600)),
            ],
        ),
    ]
