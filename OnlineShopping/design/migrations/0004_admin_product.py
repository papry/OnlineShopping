# Generated by Django 2.2 on 2019-07-20 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0003_delete_admin'),
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
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(default='', max_length=250)),
                ('description', models.CharField(default='', max_length=250)),
                ('Stock', models.IntegerField(default=20000)),
                ('Price', models.IntegerField(default='')),
                ('Category', models.ForeignKey(on_delete='CASCADE', to='design.category')),
                ('Customer', models.ForeignKey(on_delete='CASCADE', to='design.Customer')),
                ('Supplier', models.ForeignKey(on_delete='CASCADE', to='design.Supplier')),
            ],
        ),
    ]
