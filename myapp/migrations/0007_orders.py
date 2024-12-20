# Generated by Django 5.1.3 on 2024-12-03 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('order_number', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=100)),
            ],
        ),
    ]
