from django.urls import path
from .views import (
    LanguageListAPIView,
    LanguageCreateAPIView,
)

urlpatterns = [
    path('list/', LanguageListAPIView.as_view(), name='language-list'),
    path('create/', LanguageCreateAPIView.as_view(), name='language-create'),
]