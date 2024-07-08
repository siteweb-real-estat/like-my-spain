from typing import Any
from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib import messages
from dashboard.models import Booking, Property, Setting, Message
from .forms import MessageForm


class Home(ListView):
    template_name = "core/index.html"
    model = Property
    context_object_name = "properties"


class PropertyDetailView(DetailView):
    model = Property
    template_name = "core/property.html"
    context_object_name = "property"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["properties"] = Property.objects.all()
        return context


class AllProperties(ListView):
    template_name = "core/all-properties.html"
    model = Property
    context_object_name = "properties"


class PropertyListByType(ListView):
    template_name = "core/property_list_by_type.html"
    context_object_name = "properties"

    def get_queryset(self):
        property_type: str = self.kwargs["type"]
        return Property.objects.filter(property_type=property_type.capitalize())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = self.kwargs["type"]
        return context


class PropertyListByCity(ListView):
    template_name = "core/property_list_by_city.html"
    context_object_name = "properties"

    def get_queryset(self):
        city: str = self.kwargs["city"]
        return Property.objects.filter(city=city.capitalize())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["city"] = self.kwargs["city"]
        return context


class AboutUs(TemplateView):
    template_name = "core/about-us.html"


class Contacts(TemplateView):
    template_name = "core/contacts.html"


def success_page(request: HttpRequest):
    return render(request, "core/success.html")


def submit_message(request: HttpRequest):
    if request.method == "POST":
        email = request.POST.get("email-2")
        name = request.POST.get("name-2")
        message_text = request.POST.get("Message")
        print(message_text, email, name)
        message = Message.objects.create(email=email, name=name, message=message_text)
        return redirect("/success")


def submit_booking(request: HttpRequest):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        property_id = request.POST.get("property_id")
        property = get_object_or_404(Property, pk=property_id)
        booking = Booking.objects.create(email=email, name=name, property=property)
        return redirect("/success")
