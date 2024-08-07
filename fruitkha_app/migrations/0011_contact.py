# Generated by Django 5.0.2 on 2024-07-04 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruitkha_app', '0010_offer_offer_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CONTACT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('subject', models.CharField(blank=True, max_length=6, null=True)),
                ('message', models.CharField(blank=True, max_length=555, null=True)),
            ],
        ),
    ]
