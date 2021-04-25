from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_auth.registration.views import RegisterView
from rest_auth.models import TokenModel
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import (
    CustomLoginSerializer,
    CustomRegistrationSerializer,
)

class LoginTemplateView(TemplateView):
    template_name = 'user/login.html'
    extra_context = {"title": "GoCart - Login"}

class RegisterTemplateView(TemplateView):
    template_name = 'user/signup.html'
    extra_context = {"title": "GoCart - Register"}

class DashboardTemplateView(TemplateView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [BasicAuthentication,]
    template_name = 'user/dashboard.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            extra_context = {"title": "Admin Dashboard"}
        else:
            extra_context = {"title": "Error! You are not permitted to view this page."}
        return self.render_to_response(extra_context)

#
# class CustomLoginView(GenericAPIView):
#     # TODO Create Login API Endpoint
#     serializer_class = CustomLoginSerializer

"""
CUSTOM ENDPOINTS
"""

class CustomRegistrationView(RegisterView):
    serializer_class = CustomRegistrationSerializer
    # permission_classes = IsAuthenticated,
    token_model = TokenModel

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(self.get_response_data(user),
                        status=status.HTTP_201_CREATED,
                        headers=headers)