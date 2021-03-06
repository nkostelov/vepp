# Generated by Django 2.0.4 on 2018-05-18 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0009_auto_20180517_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(unique=True, verbose_name='№ договору')),
                ('date_start', models.DateField(verbose_name='дата укладання')),
                ('date_end', models.DateField(verbose_name='дата закінчення')),
                ('works', models.TextField(blank=True, help_text='заповніть через ;', verbose_name='предмет договору')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, default='0.00', max_digits=10, verbose_name='вартість робіт')),
                ('district', models.CharField(blank=True, max_length=50, verbose_name='район')),
                ('town', models.CharField(blank=True, max_length=50, verbose_name='населений пункт')),
                ('address', models.CharField(blank=True, max_length=50, verbose_name='адреса')),
                ('note', models.TextField(blank=True, verbose_name='примітка')),
            ],
        ),
        migrations.AlterField(
            model_name='firm',
            name='bank',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='crmapp.Bank', verbose_name='банк'),
        ),
        migrations.AlterField(
            model_name='firm',
            name='phone1',
            field=models.CharField(blank=True, help_text='+380665554433', max_length=16, verbose_name='номер телефона'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='bank',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='crmapp.Bank', verbose_name='банк'),
        ),
        migrations.AddField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='partner', to='crmapp.Partner', verbose_name='замовник'),
        ),
        migrations.AddField(
            model_name='contract',
            name='performer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='firm', to='crmapp.Firm', verbose_name='виконавець'),
        ),
    ]
