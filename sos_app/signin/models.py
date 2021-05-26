from django.db import models


class Picture(models.Model):
    user_id = models.IntegerField()
    image = models.ImageField()
    relation = models.CharField(max_length=255, default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.user_id


class Card(models.Model):
    user_id = models.IntegerField()
    card_first_name = models.CharField(max_length=255)
    card_last_name = models.CharField(max_length=255)
    card_text = models.TextField(default="")
    card_phone_number = models.CharField(max_length=255)
    card_region = models.CharField(max_length=255)
    relation = models.CharField(max_length=255, default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.user_id


class Region(models.Model):
    region_id = models.IntegerField()
    name = models.CharField(max_length=255)


class SenderMarkets(models.Model):
    service_id = models.IntegerField()
    name = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=255, default="")
    service_type = models.CharField(max_length=255, default="")


class Sender(models.Model):
    user_id = models.IntegerField()
    service_id = models.IntegerField()
    relation = models.CharField(max_length=255, default="")
    is_sended = models.CharField(max_length=255, default="0")


