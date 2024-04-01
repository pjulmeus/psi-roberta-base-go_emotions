from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_name, name="home"),
    path("thanks/", views.home)
   # path("your-name", views.get_name, name="home")`
]