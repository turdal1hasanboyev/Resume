from django.urls import path

from apps.resume.views import index


urlpatterns = [
    path('', index, name='home'),
]
