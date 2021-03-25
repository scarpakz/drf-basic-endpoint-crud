from django.urls import path
from .views import (
    LanguageListAPIView,
    LanguageCreateAPIView,
    LanguageRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('list/', LanguageListAPIView.as_view(), name='language-list'),
    path('create/', LanguageCreateAPIView.as_view(), name='language-create'),
    path('detail/<int:pk>/', LanguageRetrieveUpdateDestroyAPIView.as_view(), name='language-view'),
]