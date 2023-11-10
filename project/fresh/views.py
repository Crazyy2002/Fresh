from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm, AuthUserForm, RegisterUserForm
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy


# Create your views here.
def news_home(request):
    fresh = Articles.objects.all()
    return render(request, 'fresh/fresh_home.html', {'fresh': fresh});


class NewsDetailview(DetailView):
    model = Articles
    template_name = 'fresh/details_view.html'
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fresh_home')
        else:
            error = "Форма была неверной"
    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'fresh/create.html', data)


class LoginView(LoginView):
    template_name = 'fresh/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('create')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'fresh/register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('create')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class Logout(LogoutView):
    next_page = reverse_lazy('home')
