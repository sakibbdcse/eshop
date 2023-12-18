# Generated by Django 4.2.6 on 2023-10-16 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='main_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.maincategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.category'),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_quantity', models.IntegerField()),
                ('availability', models.IntegerField()),
                ('feature_image', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('product_information', models.TextField()),
                ('model_name', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.category')),
                ('sections', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.section')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=200)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.products')),
            ],
        ),
        migrations.CreateModel(
            name='Additional_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specification', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.products')),
            ],
        ),
    ]
