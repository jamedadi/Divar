# Generated by Django 3.2 on 2022-07-11 03:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='invoice_number',
            field=models.UUIDField(default=uuid.UUID('c9e8e745-f2e5-4b28-b6d2-e8150f5964d1'), verbose_name='invoice number'),
        ),
    ]