from django.shortcuts import render

# Create your views here.


def index(request):
    """
    A view to return the clubhouse index (home) page.
    """
    return render(request, 'clubhouse/index.html')


def who_we_are(request):
    """
    A view to return the 'Who We Are' information page.
    """
    return render(request, 'clubhouse/who_we_are.html')
