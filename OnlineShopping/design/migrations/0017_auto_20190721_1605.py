# Generated by Django 2.2 on 2019-07-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0016_auto_20190721_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Price',
            field=models.IntegerField(),
        ),
    ]
