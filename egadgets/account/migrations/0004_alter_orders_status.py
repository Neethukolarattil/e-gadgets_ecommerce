# Generated by Django 5.0.3 on 2024-06-05 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_products_cart_products_rename_user_cart_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('order placed', 'order placed'), ('shipped', 'shipped'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')], default='order placed', max_length=100),
        ),
    ]
