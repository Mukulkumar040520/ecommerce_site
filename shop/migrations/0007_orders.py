# Generated by Django 3.0.6 on 2020-06-09 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_delete_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=111)),
                ('email', models.CharField(max_length=111)),
                ('address', models.CharField(max_length=111)),
                ('city', models.CharField(max_length=111)),
                ('state', models.CharField(max_length=111)),
                ('zip_code', models.CharField(max_length=111)),
                ('phone', models.CharField(max_length=111)),
            ],
        ),
    ]
