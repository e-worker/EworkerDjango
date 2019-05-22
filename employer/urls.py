from django.urls import path
from . import views
from student import views as studentviews
urlpatterns = [
    path('find_student', views.find_students, name='find_student'),
    path('offer/<int:id>', views.offer, name='offer'),
    path('add_offer', views.add_offer, name="add_offer"),
    path('my_offers', views.employer_offers, name="employer_offers"),
    path('delete_offer/<int:id>', views.delete_offer, name="delete_offer"),
    path('employer_profile/<int:id>', views.employer_profile, name="employer_profile"),
    path('student_profile/<int:id>', studentviews.student_profile, name="student_profile"),

]