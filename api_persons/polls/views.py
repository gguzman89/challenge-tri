from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import requests
from .models import People, Level, Language, Course


def home(request):
    return HttpResponse('Hello World!')


def people_new(request):
    # if request.method == 'POST':
    #     name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     email = request.POST['email']
    #
    #     person = People.objects.create(
    #         first_name=name,
    #         last_name=last_name,
    #         email=email
    #     )
    # return HttpResponse('New person added...')
    return HttpResponse(People.objects.all())


def _url(path):
    return 'http://localhost:8000/api/' + path


def courses(request):
    return HttpResponse(Course.objects.all())


def languages(request):
    return HttpResponse(Language.objects.all())


def levels(request):
    return HttpResponse(Level.objects.all())


def people_find(request, person_id):
    people = get_object_or_404(People, pk=person_id)
    return HttpResponse(people)
