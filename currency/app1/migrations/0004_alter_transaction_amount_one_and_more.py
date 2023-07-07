# Generated by Django 4.2.2 on 2023-06-25 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_transaction_amount_one_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount_one',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount_two',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
