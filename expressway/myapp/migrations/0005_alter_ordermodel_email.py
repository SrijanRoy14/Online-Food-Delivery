# Generated by Django 4.1.7 on 2023-07-08 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_ordermodel_city_ordermodel_email_ordermodel_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
