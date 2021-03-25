from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    GenericAPIView,
    CreateAPIView,
)
from .serializers import (
    LanguageSerializer,
)
from .models import (
    Language,
)

class LanguageListAPIView(ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class LanguageCreateAPIView(CreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer