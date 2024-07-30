from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary.api
import cloudinary.uploader

PROPERTY_TYPE_CHOICES = [
    ("House", "House"),
    ("Apartments", "Apartments"),
    ("Commercial", "Commercial"),
    ("Land", "Land"),
]

CITY_CHOICES = [
    ("Casablanca", "Casablanca"),
    ("Rabat", "Rabat"),
    ("Fes", "Fes"),
    ("Marrakesh", "Marrakesh"),
    ("Tangier", "Tangier"),
    ("Agadir", "Agadir"),
    ("Meknes", "Meknes"),
    ("Oujda", "Oujda"),
    ("Tetouan", "Tetouan"),
    ("Kenitra", "Kenitra"),
    ("Safi", "Safi"),
    ("Nador", "Nador"),
    ("Beni Mellal", "Beni Mellal"),
    ("Taza", "Taza"),
    ("Laayoune", "Laayoune"),
    ("Dakhla", "Dakhla"),
    ("Essaouira", "Essaouira"),
    ("El Jadida", "El Jadida"),
    ("Settat", "Settat"),
    ("Mohammedia", "Mohammedia"),
]


class Property(models.Model):
    name = models.CharField(max_length=50, unique=True)
    reference = models.IntegerField(unique=True)
    property_type = models.CharField(
        max_length=50,
        choices=PROPERTY_TYPE_CHOICES,
    )
    city = models.CharField(max_length=50, choices=CITY_CHOICES, default="Casablanca")
    address = models.CharField(max_length=255, null=True)
    general_information = models.TextField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area = models.IntegerField()
    price = models.IntegerField()
    garden = models.BooleanField()
    swimming_pool = models.BooleanField()
    parking = models.BooleanField()

    class Meta:
        verbose_name_plural = "properties"

    def __str__(self):
        return f"Property('{self.name}')"


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="images"
    )
    image = CloudinaryField(resource_type='image')

    def __str__(self):
        return f"Image for Property: {self.property.name}"


from django.db import models


class Setting(models.Model):
    hero_title = models.CharField(max_length=60, null=False, blank=False)
    hero_subtitle = models.CharField(max_length=100, null=False, blank=False)
    facebook_url = models.CharField(max_length=200, null=False, blank=False)
    instagram_url = models.CharField(max_length=200, null=False, blank=False)
    phone_numbers = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    address = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return (
            self.hero_title
        )  # Display the hero title in the admin interface or wherever the model is displayed


class Message(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Message from {self.name} <{self.email}>"


class Booking(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name} <{self.email}> booking for {self.property.name}"


class Partner(models.Model):
    image = CloudinaryField(resource_type='image')
    name = models.CharField(max_length=64)
    description = models.TextField()
    phone_number = models.CharField(max_length=14)
    email = models.CharField(max_length=14)