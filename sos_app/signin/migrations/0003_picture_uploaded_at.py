# Generated by Django 3.2.3 on 2021-05-22 11:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0002_auto_20210522_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
