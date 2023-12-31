# Generated by Django 4.2.4 on 2023-09-29 18:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pronos', '0010_alter_coupon_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailparieur',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mailparieur',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
