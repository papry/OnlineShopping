# Generated by Django 2.2 on 2019-07-21 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0017_auto_20190721_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Price',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_Id',
            field=models.CharField(default='', max_length=200),
        ),
    ]
