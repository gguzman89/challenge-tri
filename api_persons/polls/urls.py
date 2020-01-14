from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'levels', views.LevelViewSet)
router.register(r'languages', views.LanguageViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'peoples', views.PeopleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
