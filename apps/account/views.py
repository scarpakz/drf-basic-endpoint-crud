from django.views.generic import TemplateView

class LoginTemplateView(TemplateView):
    template_name = 'account/login.html'
    extra_context = {"title": "GoCart - Login"}

class DashboardTemplateView(TemplateView):
    template_name = 'account/dashboard.html'
    extra_context = {"title": "Admin Dashboard"}
