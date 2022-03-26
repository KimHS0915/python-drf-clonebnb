from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('', views.UserSignupView.as_view()),
    path('token/', views.UserLoginView.as_view()),
    path('me/', views.MeView.as_view()),
    path('<int:pk>', views.UserDetailView.as_view()),
]