# Generated by Django 5.0.2 on 2024-07-04 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruitkha_app', '0011_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='enquiry_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
