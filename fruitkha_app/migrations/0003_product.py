# Generated by Django 5.0.2 on 2024-06-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruitkha_app', '0002_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PRODUCT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=30, null=True)),
                ('item_code', models.CharField(blank=True, max_length=6, null=True, unique=True)),
                ('category', models.CharField(blank=True, max_length=15, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
            ],
        ),
    ]