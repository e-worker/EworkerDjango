from django.urls import path
from . import views
from message_app import views as msg
from student import views as student_views
urlpatterns = [
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path('logout', views.logout, name='logout'),
    path("new_message", msg.new_message, name="new_message"),
    path("messages", msg.dashboard, name="messages"),
    path("chat/<int:user_id>", msg.viewMessages, name="chat"),
    path("offers", student_views.student_offers, name="offers"),
    path("profile", views.profile, name="profile"),
    path("edit_profile", student_views.edit_profile, name="edit_profile"),
    path("", views.login, name="login"),
]