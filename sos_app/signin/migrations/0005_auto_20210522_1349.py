# Generated by Django 3.2.3 on 2021-05-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0004_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='relation',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='picture',
            name='relation',
            field=models.CharField(default='', max_length=255),
        ),
    ]
