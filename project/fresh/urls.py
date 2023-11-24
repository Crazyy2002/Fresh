from django.urls import path
from . import views
from .views import delete_product, delete_product1

urlpatterns = [
    path('', views.news_home, name='fresh_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailview.as_view(), name='fresh-detail'),
    path('login', views.LoginView.as_view(), name='login_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    path('logout', views.LogoutView.as_view(), name='logout_page'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
    path('moroz/<int:category_id>/', views.category_detail1, name='moroz'),  # Updated URL
    path('moroz/delete/<int:product_id>/', delete_product1, name='delete_product1'),  # Added URL
]
