# Generated by Django 3.1.5 on 2021-01-27 11:15

import coincollection.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='coincollection.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_choice_field', models.CharField(choices=[('KP', 'KP'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='KP', max_length=2)),
                ('coin_sort_field', models.CharField(choices=[('KP', 'KP'), ('Bundeslandmünze', 'Bundeslandmünze'), ('Normale Münze', 'Normale Münze'), ('Sondermünze', 'Sondermünze')], default='KP', max_length=20)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='coin_pics')),
                ('year', models.PositiveIntegerField(default=2020, validators=[django.core.validators.MinValueValidator(1984), coincollection.models.max_value_current_year])),
                ('date_found', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='coincollection.category')),
            ],
        ),
    ]
