# Generated by Django 3.1.4 on 2021-04-01 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210317_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookstoreSeller',
            fields=[
                ('store_name', models.CharField(max_length=100)),
                ('seller_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=12)),
            ],
        ),
    ]
