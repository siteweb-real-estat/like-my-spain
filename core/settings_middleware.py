from dashboard.models import Setting


class SettingsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        settings = Setting.objects.first()
        request.settings = settings
        request.settings.phone_numbers= request.settings.phone_numbers.split(', ')
        request.CITY_CHOICES = [
            ("Madrid", "Madrid"),
            ("Barcelona", "Barcelona"),
            ("Valencia", "Valencia"),
            ("Seville", "Seville"),
            ("Bilbao", "Bilbao"),
            ("Malaga", "Malaga"),
            ("Granada", "Granada"),
            ("Alicante", "Alicante"),
            ("Cordoba", "Cordoba"),
            ("Zaragoza", "Zaragoza"),
        ]

        response = self.get_response(request)
        return response
