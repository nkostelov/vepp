# Generated by Django 2.0.4 on 2018-06-05 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0027_auto_20180605_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crmapp.Services', verbose_name='робота'),
        ),
    ]
