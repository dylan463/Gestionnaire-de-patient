# Generated by Django 4.2.14 on 2024-07-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='contact',
            field=models.CharField(default='', max_length=14),
        ),
    ]
