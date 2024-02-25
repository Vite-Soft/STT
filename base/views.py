from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = "pages/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["company_name"] = "My Awesome Company"
    #     context["description"] = "We provide amazing products and services."
    #     return context

class RegisterView(FormView):
    template_name = 'pages/auth/register.html'
    form_class = UserCreationForm
    success_url = 'login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
class CustomLoginView(LoginView):
    template_name = 'pages/auth/login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True
    
    def get_success_url(self):
        # Implement your custom redirection logic here
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        # Default redirect based on user type or other criteria
        return reverse_lazy('home')

class CustomLogoutView(LogoutView):
    # next_page = reverse_lazy('home')
    template_name = 'pages/auth/logout.html'
    