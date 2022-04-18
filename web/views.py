from django.http import HttpResponse
from django.shortcuts import render
from .models import Person


def index(request):
    return HttpResponse("Hello world.")


def persons(request):
    all_entries = Person.objects.all()
    context = {'persons': all_entries}
    return render(request, 'person.html', context)
