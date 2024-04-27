from django.urls import reverse_lazy
from django.views.generic.edit import CreateView 
from .forms import AccountCreationForm
# Create your views here.

class AccountRegisterView(CreateView):
    form_class = AccountCreationForm
    success_url = reverse_lazy("login")
    template_name = 'register.html'