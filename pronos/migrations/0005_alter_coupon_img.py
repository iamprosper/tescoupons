# Generated by Django 4.2.4 on 2023-09-14 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pronos', '0004_alter_coupon_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='img',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
