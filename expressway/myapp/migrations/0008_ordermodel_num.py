# Generated by Django 4.1.7 on 2023-07-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_name_adminuser_pwd'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='num',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
