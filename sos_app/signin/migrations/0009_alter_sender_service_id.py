# Generated by Django 3.2.3 on 2021-05-25 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0008_card_card_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sender',
            name='service_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signin.sendermarkets'),
        ),
    ]