from django.urls import path
from . import views
urlpatterns = [
    path('', views.edit_profile, name="edit_profile"),
    path('offers', views.student_offers, name="student_offers"),
    path('profil', views.student_profile, name="student_profile"),
]