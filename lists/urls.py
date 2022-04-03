from rest_framework.routers import DefaultRouter
from . import views

app_name = 'lists'

router = DefaultRouter()
router.register('', views.ListViewSet)

urlpatterns = router.urls
