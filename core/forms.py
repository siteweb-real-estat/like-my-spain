from django import forms
from django.db import models

from dashboard.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["email", "message", "name"]  # Specify fields from your Message model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize form labels, placeholders, or other attributes if needed
        self.fields["email"].widget.attrs.update({"placeholder": "Enter your email"})
        self.fields["name"].widget.attrs.update({"placeholder": "Enter your name"})
