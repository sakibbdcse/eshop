# Generated by Django 4.2.6 on 2023-10-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_products_packing_cost_products_tax'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=150)),
                ('discount', models.IntegerField()),
            ],
        ),
    ]
