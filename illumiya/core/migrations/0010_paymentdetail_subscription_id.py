# Generated by Django 2.2.6 on 2020-01-18 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200118_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetail',
            name='subscription_id',
            field=models.CharField(default='2', max_length=200),
            preserve_default=False,
        ),
    ]
