from .models import Setting


class SettingsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        settings = Setting.objects.first()
        request.settings = settings
        request.settings.phone_numbers= request.settings.phone_numbers.split(', ')
        request.CITY_CHOICES = [
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

        response = self.get_response(request)
        return response
