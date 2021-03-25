from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import (
    LanguageSerializer,
)
from .models import (
    Language,
)

class LanguageListAPIView(ListAPIView):
    # permission_classes = IsAuthenticated,
    # authentication_classes = TokenAuthentication
    # authentication_classes = JWTAuthentication,
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class LanguageCreateAPIView(CreateAPIView):
    # permission_classes = IsAuthenticated,
    # authentication_classes = TokenAuthentication
    # authentication_classes = JWTAuthentication,
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class LanguageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes = IsAuthenticated,
    # authentication_classes = TokenAuthentication
    # authentication_classes = JWTAuthentication,
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer