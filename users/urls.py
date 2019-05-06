from django.urls import path
from . import views
from message_app import views as msg
urlpatterns = [
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path('logout', views.logout, name='logout'),
    path("new_message", msg.new_message, name="new_message"),
    path("messages", msg.dashboard, name="messages"),
    path("chat/<int:user_id>", msg.viewMessages, name="chat"),
    path("offers", views.offers, name="offers"),
    path("profile", views.profile, name="profile"),
]