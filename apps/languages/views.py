from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, GenericAPIView
from .serializers import (
    LanguageSerializer,
)
from .models import (
    Language,
)

class LanguageAPIView(ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer