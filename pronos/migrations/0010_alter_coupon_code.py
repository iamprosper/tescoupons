# Generated by Django 4.2.4 on 2023-09-16 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pronos', '0009_coupon_updated_at_alter_coupon_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(blank=True, help_text='Uniquement requis pour le bookmaker 1xbet', max_length=5),
        ),
    ]
