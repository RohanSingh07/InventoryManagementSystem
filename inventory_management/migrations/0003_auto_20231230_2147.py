# Generated by Django 3.2 on 2023-12-30 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0002_alter_product_sellername'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='video',
        ),
    ]