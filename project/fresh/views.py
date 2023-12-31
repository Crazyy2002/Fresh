from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles, Category
from .forms import ArticlesForm, AuthUserForm, RegisterUserForm
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import ArticlesForm
from django.contrib import messages


# Create your views here.
def news_home(request):
    fresh = Articles.objects.all()
    return render(request, 'main/product.html', {'fresh': fresh});


class NewsDetailview(DetailView):
    model = Articles
    template_name = 'fresh/create.html'
    context_object_name = 'article'


def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно добавлен!')
            return redirect('create')
        else:
            messages.error(request, 'Форма была неверной')

    form = ArticlesForm()
    return render(request, 'fresh/create.html', {'form': form})


class LoginView(LoginView):
    template_name = 'fresh/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'fresh/register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')
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


def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.articles_set.filter(category_id=1).order_by('date1')  # Сортировка по убыванию даты
    now = datetime.now().date()  # Текущая дата

    products_with_days = []
    for product in products:
        days_until_expiration = (product.date1 - now).days
        products_with_days.append({'product': product, 'days_until_expiration': days_until_expiration})

    return render(request, 'fresh/category_detail.html', {'category': category, 'products_with_days': products_with_days, 'now': now})

def delete_product(request, product_id):
    product = get_object_or_404(Articles, id=product_id)
    product.delete()
    return redirect('category_detail', category_id=1)


def category_detail1(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.articles_set.filter(category_id=2).order_by('date1')  # Сортировка по убыванию даты
    now = datetime.now().date()  # Текущая дата

    products_with_days = []
    for product in products:
        days_until_expiration = (product.date1 - now).days
        products_with_days.append({'product': product, 'days_until_expiration': days_until_expiration})

    return render(request, 'fresh/moroz.html', {'category': category, 'products_with_days': products_with_days, 'now': now})

def delete_product1(request, product_id):
    product = get_object_or_404(Articles, id=product_id)
    product.delete()
    return redirect('moroz', category_id=2)

def category_detail2(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.articles_set.filter(category_id=3).order_by('date1')  # Сортировка по убыванию даты
    now = datetime.now().date()  # Текущая дата

    products_with_days = []
    for product in products:
        days_until_expiration = (product.date1 - now).days
        products_with_days.append({'product': product, 'days_until_expiration': days_until_expiration})

    return render(request, 'fresh/cupboard.html', {'category': category, 'products_with_days': products_with_days, 'now': now})

def delete_product2(request, product_id):
    product = get_object_or_404(Articles, id=product_id)
    category_id = product.category_id  # Получаем ID категории из продукта
    product.delete()
    return redirect(reverse('cupboard', kwargs={'category_id': category_id}))