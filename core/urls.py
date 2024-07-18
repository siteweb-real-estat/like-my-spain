from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path("", views.Home.as_view(), name="index"),
    path("all-properties", views.AllProperties.as_view(), name="all_properties"),
    path("property/<reference>", views.PropertyDetailView.as_view(), name="property"),
    path("contacts/", views.Contacts.as_view(), name="contacts"),
    path("success/", views.success_page, name="success_page"),
    path("about-us/", views.AboutUs.as_view(), name=""),
    path("submit-message/", views.submit_message, name="submit_message"),
    path("submit-booking/", views.submit_booking, name="submit_booking"),
    path("type/<type>/", views.PropertyListByType.as_view(), name="property_type"),
    path("city/<str:city>/", views.PropertyListByCity.as_view(), name="property_city"),
    path('download-backup/', views.download_backup, name='download_backup'),
]
