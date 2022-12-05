# Generated by Django 4.1.2 on 2022-12-04 19:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homee', '0003_detail_foodtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='FoodType',
        ),
        migrations.AddField(
            model_name='detail',
            name='Reg_No',
            field=models.CharField(choices=[('CST/19/IFT/00405', 'CST/19/IFT/00405'), ('CST/19/IFT/00408', 'CST/19/IFT/00408'), ('CST/19/SWE/00403', 'CST/19/SWE/00403'), ('CST/19/IFT/00404', 'CST/19/IFT/00404'), ('CST/19/IFT/00403', 'CST/19/IFT/00403'), ('CST/19/IFT/00412', 'CST/19/IFT/00412')], default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
