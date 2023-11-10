from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='fresh_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailview.as_view(), name='fresh-detail'),
    path('login', views.LoginView.as_view(), name='login_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    path('logout', views.LogoutView.as_view(), name='logout_page'),
]
