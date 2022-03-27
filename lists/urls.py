from django.urls import path
from . import views

app_name = 'lists'

urlpatterns = [
    path('', views.ListView.as_view()),
]