from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework import generics
from django.contrib.auth import authenticate

from .models import *
from .forms import *
from rest_framework.renderers import JSONRenderer
from .serializers import *
import json


class IndexView(ListView):
    model = Brand
    template_name = "platinum/index.html"
    context_object_name = "brands"


class OilDetailView(DetailView):
    model = Oil

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["oil_instances"] = OilInstance.objects.all()
        context["standards"] = Standard.objects.all()
        return context


class BrandDetailView(DetailView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["motor_oils"] = Oil.objects.filter(type__icontains="motor")
        context["transmission_oils"] = Oil.objects.filter(type__icontains="trans")
        context["standards"] = Standard.objects.all()
        return context


def contacts(request):
    context = {
        "phone": "(099) 999-99-99",
        "address": "Восточная ул., 9, Запорожье, Запорожская область, 69000",
        "manager": "Revenets Dmytrij",
    }
    return render(request, "platinum/contacts.html", context)


def search(request):
    string = request.POST.get("search")

    if string:
        context = {
            "string": string,
            "brands": Brand.objects.filter(name__icontains=string),
            "oils": Oil.objects.filter(Q(w_visco__icontains=string[:1]) | Q(s_visco__icontains=string[-2:])),
        }
        return render(request, 'platinum/search.html', context)
    return HttpResponseRedirect(reverse("platinum:index"))


def cart(request):
    context = {
        "order_form": CartModelForm(),
        "order": Cart.objects.filter(status__iexact="w"),

    }
    return render(request, "platinum/cart.html", context)


def add_order(request):
    form = CartModelForm(request.POST)
    saved = form.save(commit=False)
    saved.save()
    return HttpResponseRedirect(reverse("platinum:cart"))


def process_order(request):
    orders = Cart.objects.filter(status__iexact="w")
    order = {
        "name": [],
        "oil": [],
        "amount": [],
        "price": [],
    }
    for data in orders:
        order["oil"].append(str(data.oil))
        order["amount"].append(data.amount)
        if request.user.is_authenticated:
            order["name"].append(str(request.user.get_full_name()))
            order["price"].append(data.oil.get_discount())
        data.status = "d"
        data.save()
    order_list = {
        "order": order,
    }
    with open("order.json", "a", newline="\n") as file:
        json.dump(order_list, file, indent=3)
    return HttpResponseRedirect(reverse("platinum:index"))
