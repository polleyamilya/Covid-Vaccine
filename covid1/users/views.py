from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import covidvacc, State
from .forms import covidForm
from django.shortcuts import render

def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})

class CovidListView(ListView):
    model = covidvacc
    form_class = covidForm
    context_object_name = 'covidvacc'

class CovidCreateView(CreateView):
    model = covidvacc
    form_class = covidForm
    success_url = reverse_lazy('covid_changelist')

class CovidUpdateView(UpdateView):
    model = covidvacc
    form_class = covidForm
    success_url = reverse_lazy('covid_changelist')


def load_stateless(request):
    district_id = request.GET.get('district')
    stateless = State.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'state.html', {'stateless': stateless})
@login_required()
def profile(request):
    return render(request, 'profile.html','state.html')

