from django.utils.cache import add_never_cache_headers

class NoCacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response

# class DisableClientSideCachingMiddleware(object):
#     def process_response(self, request, response):
#         add_never_cache_headers(response)
#         return response
    
class DisableClientSideCachingMiddleware:
    """
    Middleware to disable client side caching, that is on browser.
    Adds a Cache-Control: max-age=0, no-cache, no-store, must-revalidate, private header ,
    to a response to indicate that a page should never be cached.

    If not added and the api returns a cached response, the browser also caches the data into disk cache.
    Meaning we don't want caching to happen at browser level on client side as clinent will see data from
    disk cache even if it is changed on server side.

    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        add_never_cache_headers(response)
        return response
