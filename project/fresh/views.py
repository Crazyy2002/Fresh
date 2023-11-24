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


def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.articles_set.filter(category_id=2).order_by('date1')  # Сортировка по убыванию даты
    now = timezone.now()  # Текущая дата
    products_with_days = [
        {'product': product, 'days_until_expiration': (product.date1 - now.date()).days}
        for product in products
    ]
    return render(request, 'fresh/category_detail.html', {'category': category, 'products': products, 'now': now})
def delete_product(request, product_id):
    product = get_object_or_404(Articles, id=product_id)
    product.delete()
    return redirect('category_detail', category_id=2)

def category_detail1(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.articles_set.filter(category_id=3)  # Измените на нужный идентификатор категории
    return render(request, 'fresh/moroz.html', {'category': category, 'products': products})

def delete_product1(request, product_id):
    product = get_object_or_404(Articles, id=product_id)
    category_id = product.category.id  # Get the category ID before deletion
    product.delete()
    return redirect('moroz', category_id=category_id)  # Redirect to the 'moroz' view with the correct category ID



