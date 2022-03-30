from django.urls import path
from reviews import views as review_views
from . import views

app_name = 'rooms'

urlpatterns = [
    path('', views.RoomListView.as_view()),
    path('search/', views.RoomSearchView.as_view()),
    path('<int:pk>/', views.RoomDetailView.as_view()),
    path('<int:pk>/reviews', review_views.room_reviews),
]