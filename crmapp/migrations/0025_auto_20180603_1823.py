# Generated by Django 2.0.4 on 2018-06-03 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0024_auto_20180603_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(default='0', max_length=3, verbose_name='прогрес'),
        ),
    ]
