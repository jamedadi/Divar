# Generated by Django 3.2 on 2022-05-01 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0007_auto_20220501_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisementimage',
            name='name',
            field=models.CharField(default='test1', max_length=50),
        ),
    ]