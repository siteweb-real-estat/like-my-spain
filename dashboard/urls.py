from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path("", views.Dashboard.as_view(), name="dashboard"),
    path(
        "login/", LoginView.as_view(template_name="dashboard/login.html"), name="login"
    ),
    path("properties/", views.PropertyListView.as_view(), name="property_list"),
    path(
        "properties/create/", views.PropertyCreateView.as_view(), name="property_create"
    ),
    # path('properties/create/', views.PropertyCreateView.as_view() , name='property_create'),
    path(
        "properties/update/<pk>",
        views.PropertyUpdateView.as_view(),
        name="property_update",
    ),
    # path('delete-image/<pk>', views.delete_property_image , name='delete_image'),
    path("settings/", views.SettingUpdateView.as_view(), name="settings_update"),
]

# 8008
