from django.urls import path
from .views import (
    LoginTemplateView,
    DashboardTemplateView,
    RegisterTemplateView,
    CustomRegistrationView,
)

urlpatterns = [
    path('', LoginTemplateView.as_view(), name='login'),
    path('register/', RegisterTemplateView.as_view(), name='register'),
    path('dashboard/', DashboardTemplateView.as_view(), name='dashboard'),

    path('api/v1/registration-view/', CustomRegistrationView.as_view(), name='registration'),
]