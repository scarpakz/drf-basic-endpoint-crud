from django.urls import path
from .views import (
    LanguageAPIView,
)

urlpatterns = [
    path('languages/', LanguageAPIView.as_view(), name='language-list'),
]