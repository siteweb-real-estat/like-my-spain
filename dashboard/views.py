from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.shortcuts import redirect, render
from django.forms import inlineformset_factory
from .models import Property, PropertyImage, Setting
from .forms import PropertyForm, PropertyImageForm, SettingForm

# Define the inline formset for PropertyImage
PropertyImageFormSet = inlineformset_factory(
    Property, PropertyImage, form=PropertyImageForm, extra=1
)


class Dashboard(TemplateView):
    template_name = "dashboard/index.html"


class PropertyCreateView(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = "dashboard/property_form.html"
    success_url = reverse_lazy(
        "property_list"
    )  # Use the name of your URL pattern for the property list view

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["images_formset"] = PropertyImageFormSet(
                self.request.POST, self.request.FILES
            )
        else:
            data["images_formset"] = PropertyImageFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        images_formset = context["images_formset"]
        if form.is_valid() and images_formset.is_valid():
            self.object = form.save()
            images_formset.instance = self.object
            images_formset.save()
            messages.success(self.request, "Property and images saved successfully!")
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class PropertyUpdateView(UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = "dashboard/property_form.html"
    success_url = reverse_lazy(
        "property_list"
    )  # Use the name of your URL pattern for the property list view

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["images_formset"] = PropertyImageFormSet(
                self.request.POST, self.request.FILES
            )
        else:
            data["images_formset"] = PropertyImageFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        images_formset = context["images_formset"]
        if form.is_valid() and images_formset.is_valid():
            self.object = form.save()
            images_formset.instance = self.object
            images_formset.save()
            messages.success(self.request, "Property and images saved successfully!")
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class PropertyListView(ListView):
    model = Property
    template_name = "dashboard/property_list.html"


class SettingUpdateView(UpdateView):
    model = Setting
    form_class = SettingForm
    template_name = "dashboard/settings.html"
    success_url = reverse_lazy(
        "dashboard"
    )  # Redirect URL upon successful form submission

    def get_object(self, queryset=None):
        # Get the existing setting or create a new one if it doesn't exist
        return Setting.objects.first() or Setting.objects.create()

    def get_initial(self):
        default_data = {
            "hero_title": "Find your next perfect place to live",
            "hero_subtitle": "We have more than 500 luxury properties for you",
            "facebook_url": "http://facebook.com/",
            "instagram_url": "http://instagram.com/",
            "phone_numbers": "+34 633 35 01 00",
            "email": "likemyspain@gmail.com",
            "address": "Carrer del Call, 30, 08002 Barcelona, Spain",
        }
        setting = self.object  # The object being edited in the form
        initial_data = {
            key: getattr(setting, key, default_data[key]) for key in default_data
        }
        return initial_data
