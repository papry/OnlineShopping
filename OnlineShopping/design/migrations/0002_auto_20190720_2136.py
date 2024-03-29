# Generated by Django 2.2 on 2019-07-20 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admin_name', models.CharField(default='', max_length=250)),
                ('Password', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_name', models.CharField(default='', max_length=250)),
                ('Email', models.CharField(default='', max_length=250)),
                ('Password', models.CharField(default='', max_length=250)),
                ('Phone_no', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.IntegerField(default='')),
                ('Quantity', models.CharField(default='', max_length=250)),
                ('price', models.CharField(default='', max_length=250)),
                ('total', models.IntegerField(default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.AlterField(
            model_name='supplier',
            name='Phone_no',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
