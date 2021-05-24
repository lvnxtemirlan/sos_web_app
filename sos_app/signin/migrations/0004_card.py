# Generated by Django 3.2.3 on 2021-05-22 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0003_picture_uploaded_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=255)),
                ('card_first_name', models.CharField(max_length=255)),
                ('card_last_name', models.CharField(max_length=255)),
                ('card_phone_number', models.CharField(max_length=255)),
                ('card_region', models.CharField(max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
