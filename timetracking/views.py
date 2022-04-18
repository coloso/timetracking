from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")


def time_tracking(request):
    return HttpResponse("This is my first page.")
