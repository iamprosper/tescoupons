# Generated by Django 4.2.4 on 2023-09-15 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pronos', '0008_alter_coupon_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
