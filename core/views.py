import os
from typing import Any
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Booking, Property, Setting, Message
from django.core import management

class Home(ListView):
    template_name = "core/index.html"
    model = Property
    context_object_name = "properties"

class PropertyDetailView(DetailView):
    template_name = 'core/property.html'
    model = Property
    context_object_name = 'property'

    def get_object(self, queryset=None):
        reference = self.kwargs.get('reference')  # Extract the reference from URL kwargs
        obj = Property.objects.get(reference=reference)  # Fetch the property by reference
        return obj
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["properties"] = Property.objects.all()[:3]
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


def download_backup(request):
    # Define paths to backup files
    db_backup_file = os.path.join(settings.BASE_DIR, 'backup.json')

    # Create a new database backup
    management.call_command('dumpdata', '--output', db_backup_file)
    
    # Serve the backup JSON file for download
    if os.path.exists(db_backup_file):
        with open(db_backup_file, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename=backup.json'
            
            
            return response
    else:
        return HttpResponse("Backup file not found", status=404)
    

# def handler404(request, *args, **argv):
#     return render(request, 'core/404.html', {})