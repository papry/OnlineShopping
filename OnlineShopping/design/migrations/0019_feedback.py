# Generated by Django 2.2 on 2019-07-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0018_auto_20190721_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('email', models.CharField(default='', max_length=250)),
                ('message', models.CharField(default='', max_length=250)),
            ],
        ),
    ]
