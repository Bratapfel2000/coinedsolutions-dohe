# Generated by Django 3.1.5 on 2021-05-27 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coincollection', '0003_auto_20210218_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='coin_choice_field',
            field=models.CharField(choices=[('KP', 'KP'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('J', 'J'), ('M', 'M'), ('R', 'R')], default='KP', max_length=2),
        ),
    ]
