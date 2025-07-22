"""Views to handle errors"""
from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """ Error Handler 500 - Internal Server Error """
    return render(request, "errors/500.html", status=500)


def trigger_error(request):
    # Raise an error intentionally to test 500 page
    raise Exception("Testing 500 error page")