# Generated by Django 2.2 on 2019-07-21 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0013_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(default=1),
        ),
    ]
