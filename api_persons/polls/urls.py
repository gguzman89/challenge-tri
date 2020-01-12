from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('languages/', views.languages, name='languages'),
    path('levels/', views.levels, name='levels'),
    path('peoples/', views.people_new, name='people_new'),
    path('peoples/<int:person_id>/', views.people_find, name='people_find'),

]
