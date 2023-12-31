# Generated by Django 4.1.1 on 2023-04-19 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_constructor', '0005_alter_tgpayment_options_remove_tgpayment_bot_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tgpayment',
            name='fact_amt',
            field=models.BigIntegerField(default=0, verbose_name='TGPayment fact amt'),
        ),
        migrations.AlterField(
            model_name='tgpayment',
            name='amt',
            field=models.BigIntegerField(default=0, verbose_name='TGPayment amt'),
        ),
    ]
