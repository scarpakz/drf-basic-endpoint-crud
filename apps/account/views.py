from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import (
    CustomLoginSerializer,
)

class LoginTemplateView(TemplateView):
    template_name = 'account/login.html'
    extra_context = {"title": "GoCart - Login"}

class DashboardTemplateView(TemplateView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [BasicAuthentication,]
    template_name = 'account/dashboard.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            extra_context = {"title": "Admin Dashboard"}
        else:
            extra_context = {"title": "Error! You are not permitted to view this page."}
        return self.render_to_response(extra_context)

class CustomLoginView(GenericAPIView):
    # TODO Create Login API Endpoint
    serializer_class = CustomLoginSerializer