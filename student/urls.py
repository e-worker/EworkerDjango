from django.urls import path
from . import views
urlpatterns = [
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('offers', views.student_offers, name="student_offers"),
    path('student_profile/<int:id>', views.student_profile, name="student_profile"),
    path('match', views.match_offer_with_student, name="match_offers"),
    
]