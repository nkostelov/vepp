# Generated by Django 2.0.4 on 2018-04-17 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='дата народження'),
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='phone2',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='номер телефона'),
        ),
    ]
