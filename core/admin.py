from django.contrib import admin
from .models import Booking, Property, Setting, Message, PropertyImage
from unfold.admin import ModelAdmin, TabularInline
from django.contrib.auth.models import Group, User

admin.site.site_header = "IMOSAKI"
admin.site.site_title = "IMOSAKI"
admin.site.name = "IMOSAKI"


class PropertyImageInline(TabularInline):
    model = PropertyImage
    extra = 1


@admin.register(Property)
class PropertyAdmin(ModelAdmin):
    list_display = ["name", "reference", "property_type", "city"]
    inlines = [PropertyImageInline]


@admin.register(Setting)
class SettingAdmin(ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(ModelAdmin):
    list_editable = []
    readonly_fields = [field.name for field in Message._meta.get_fields()]

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    list_editable = []
    readonly_fields = [field.name for field in Booking._meta.get_fields()]

    def has_add_permission(self, request, obj=None):
        return False


admin.site.unregister(User)
admin.site.unregister(Group)
# admin.site.register(Message)
