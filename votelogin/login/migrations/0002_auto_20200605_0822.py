# Generated by Django 2.2.7 on 2020-06-05 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='staff'),
        ),
    ]
