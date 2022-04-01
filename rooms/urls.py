from django.urls import path
from rest_framework.routers import DefaultRouter
from reviews import views as review_views
from . import views

app_name = 'rooms'

router = DefaultRouter()
router.register('', views.RoomViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('<int:pk>/reviews', review_views.room_reviews),
]
