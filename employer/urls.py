from django.urls import path
from . import views
urlpatterns = [
    path('find_student', views.find_students, name='find_student'),
    path('offer', views.offer, name='offer'),
]