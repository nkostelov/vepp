# Generated by Django 2.0.4 on 2018-04-21 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20180417_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectuser',
            name='is_assistant',
            field=models.BooleanField(default=False, verbose_name='помічник'),
        ),
    ]