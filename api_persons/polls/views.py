from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import People, Level, Language, Course
from rest_framework import viewsets
from .serializers import LevelSerializer, LanguageSerializer, CourseSerializer, PeopleSerializer


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
    if request.method == 'POST':
        code = request.POST['code']
        name = request.POST['name']

        language = Language.objects.create(
            code=code,
            name=name
        )

        return HttpResponse('Eureka!')

    peoples = get_list_or_404(People)
    return HttpResponse(peoples)


def _url(path):
    return 'http://localhost:8000/api/' + path


def courses(request):
    return HttpResponse(Course.objects.all())


def languages(request):
    return HttpResponse(Language.objects.all())


def levels(request):
    return HttpResponse(Level.objects.all())


def people_find(request, person_id):
    person = get_object_or_404(People, pk=person_id)
    return HttpResponse(person)


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all().order_by('id')
    serializer_class = LevelSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all().order_by('code')
    serializer_class = LanguageSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('name')
    serializer_class = CourseSerializer


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
