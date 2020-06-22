# Generated by Django 2.0.2 on 2019-12-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('itemsJson', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(default='', max_length=20)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=12)),
            ],
        ),
    ]
