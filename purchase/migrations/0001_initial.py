# Generated by Django 3.2 on 2022-07-11 03:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('package', '0001_initial'),
        ('advertisement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('financial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.BigIntegerField(verbose_name='price')),
                ('status', models.SmallIntegerField(choices=[(10, 'Paid'), (-10, 'Not Paid')], default=-10, verbose_name='status')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified_time')),
                ('advertisement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchases', to='advertisement.advertisement', verbose_name='advertisement')),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchases', to='package.package', verbose_name='package')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='purchases', to='financial.payment', verbose_name='payment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchases', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'purchase',
                'verbose_name_plural': 'purchases',
            },
        ),
    ]
