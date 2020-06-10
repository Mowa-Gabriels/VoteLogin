from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from .models import Poll,Option


def home(request):
    polls = Poll.objects.all()
    option = Option.objects.all()
    context = {
        'polls': polls,
        'option': option
    }
    return render(request, 'home.html', context)


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

