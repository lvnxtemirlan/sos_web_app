from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Picture, Region, Card, SenderMarkets, Sender
from django.core import serializers
import json
from .send_email import send_email
from .forms import SignUpForm, PictureForm, CardForm, ServiceForm

from decouple import config
from .bot import Alerter

TELEGRAM_CHAT_ID = config("TELEGRAM_CHAT_ID")


# @login_required
def home(request):
    p = []
    try:
        p = Region.objects.all()
    except:
        pass


    return render(request, "home.html", {"region": p})


def card(request):
    c, p = {}, {}
    cards = []
    try:
        c = Card.objects.filter(user_id=request.user.id).all()
        p = Picture.objects.filter(user_id=request.user.id).all()
        r = Region.objects.all()
        regions = {repr(i.region_id): i.name for i in r}
        count = 1
        for card in c:
            for picture in p:
                if card.relation == picture.relation:
                    count += 1
                    cards.append({
                        "card_number": count,
                        "card_first_name": card.card_first_name,
                        "card_last_name": card.card_last_name,
                        "card_created": card.uploaded_at,
                        "card_text": card.card_text,
                        "card_region": regions.get(card.card_region, "Unselect region"),
                        "card_phone_number": card.card_phone_number,
                        "card_relation": card.relation
                    })
    except:
        pass

    return render(request, "list.html", {"cards": cards})


def card_view(request, relation):
    c = Card.objects.get(relation=relation)
    p = Picture.objects.get(relation=relation)
    s = SenderMarkets.objects.all()
    try:
        ss = Sender.objects.all().filter(relation=relation)
        sender_serialized = serializers.serialize("json", ss)
        sender = json.loads(sender_serialized)
    except:
        sender = []
    card_serialized = serializers.serialize("json", [c, ])
    picture_serialized = serializers.serialize("json", [p, ])
    sender_market_serialized = serializers.serialize("json", s)

    card = json.loads(card_serialized)[0]
    picture = json.loads(picture_serialized)[0]
    picture["url"] = p.image.url
    sender_market = json.loads(sender_market_serialized)
    for idx, market in enumerate(sender_market):
        is_sended = False
        for service in sender:
            if market["fields"]["service_id"] == service["fields"]["service_id"]:
                if service["fields"]["is_sended"] == "1":
                    is_sended = True
        if is_sended:
            market["fields"]["is_sended"] = "1"
        else:
            market["fields"]["is_sended"] = "0"
    print(sender)
    print("card", card)
    print("picture", picture)
    return render(request, "card_view.html", {"card": card, "picture": picture, "sender_market": sender_market})


def send_services(request):
    data = {}
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            send_telegram(request.POST.get("relation"))

            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            return JsonResponse(data)


def send_telegram(relation):
    c = Card.objects.get(relation=relation)
    p = Picture.objects.get(relation=relation)
    r = Region.objects.all()
    regions = {repr(i.region_id): i.name for i in r}
    try:
        ss = Sender.objects.get(relation=relation, is_sended="0", service_id=1)
    except:
        ss = []
    sender_serialized = serializers.serialize("json", [ss, ])
    sender = json.loads(sender_serialized)
    print(sender)
    alert = Alerter(chat_id=TELEGRAM_CHAT_ID)
    alert.send_photo(msg=f"Нужна помощь!!! \nДля {c.card_last_name} {c.card_first_name} \n"
                         f"По номеру: {c.card_phone_number} \n", image_path=p.image.path)



@csrf_protect
def add_image(request):
    data = {}
    form = PictureForm()
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        print("POST", request.POST)
        print("FILES", request.FILES)
        print(form, form.is_valid(), "form_image")
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['picture_form'] = render_to_string("home.html",
                                               {'form': form}, request=request)

    data['picture_form'] = render_to_string("home.html",
                                               {'form': form}, request=request)
    return JsonResponse(data)


@csrf_protect
def add_card(request):
    data = {}
    if request.method == "POST":
        form = CardForm(request.POST, request.FILES)
        print("Add card post", request.POST)
        print("Add card form", form)
        if form.is_valid():
            print("Add card form is valid")
            form.save()
            data["form_is_valid"] = True
            return JsonResponse(data)
        else:
            print("Add card form is not valid")
            data["form_is_valid"] = False
            return  JsonResponse(data)

    data = {}
    return render(request, "home.html", {"form": {}})



def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})
