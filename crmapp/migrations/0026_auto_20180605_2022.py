# Generated by Django 2.0.4 on 2018-06-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0025_auto_20180603_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='date_create',
            field=models.DateField(default='2018-06-05', verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_create',
            field=models.DateField(default='2018-06-05', verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_create',
            field=models.DateField(default='2018-06-05', verbose_name='дата створення'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_create',
            field=models.DateField(default='2018-06-05', verbose_name='дата створення'),
        ),
    ]