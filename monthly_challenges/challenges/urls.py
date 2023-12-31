from django.urls import path
from . import views

# url config
urlpatterns = [
    # takes 3 args (string of url, view function, name of url)
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challenge_by_int),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
