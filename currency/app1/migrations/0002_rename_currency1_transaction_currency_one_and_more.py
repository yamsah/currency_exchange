# Generated by Django 4.2.2 on 2023-06-25 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='currency1',
            new_name='currency_one',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='currency2',
            new_name='currency_two',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='price1',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='price2',
        ),
        migrations.AddField(
            model_name='transaction',
            name='amount_one',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='transaction',
            name='amount_two',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='transaction',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
