# forms.py
from django import forms
from .models import Property, PropertyImage, Setting
from django.forms import inlineformset_factory


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = "__all__"
        # widgets =


class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = "__all__"


PropertyImageFormSet = inlineformset_factory(
    Property, PropertyImage, form=PropertyImageForm, extra=1
)


class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = "__all__"
