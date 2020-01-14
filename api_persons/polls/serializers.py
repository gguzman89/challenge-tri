from .models import Course, Level, Language, People
from rest_framework import serializers


class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ['name']


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ['code', 'name']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'language_code', 'level_id', 'created_at', 'updated_at', '_level', 'language']


class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = People
        fields = ['first_name', 'last_name', 'email', 'created_at', 'updated_at', 'courses']
