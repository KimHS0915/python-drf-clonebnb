from django.urls import path
from rest_framework.routers import DefaultRouter
from reviews import views as review_views
from . import views

app_name = 'rooms'

router = DefaultRouter()
router.register('', views.RoomViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('search/', views.RoomSearchView.as_view()),
    path('<int:pk>/reviews', review_views.room_reviews),
]

# urlpatterns = [
#     path('', views.RoomListView.as_view()),
#     path('search/', views.RoomSearchView.as_view()),
#     path('<int:pk>/', views.RoomDetailView.as_view()),
#     path('<int:pk>/reviews', review_views.room_reviews),
# ]