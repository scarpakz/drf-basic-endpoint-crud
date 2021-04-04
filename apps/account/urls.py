from django.urls import path
from .views import (
    LoginTemplateView,
    DashboardTemplateView,
)

urlpatterns = [
    path('', LoginTemplateView.as_view(), name='login'),
    path('dashboard/', DashboardTemplateView.as_view(), name='dashboard'),
]