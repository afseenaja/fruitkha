# Generated by Django 5.0.2 on 2024-06-29 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruitkha_app', '0007_remove_offer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='offer_rate',
            new_name='percentage',
        ),
        migrations.AddField(
            model_name='offer',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
