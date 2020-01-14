from .models import People, Level, Language, Course
from rest_framework import viewsets
from .serializers import LevelSerializer, LanguageSerializer, CourseSerializer, PeopleSerializer


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
