from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная Страница',

    }
    return render(request, 'main/index.html', data)
def main(request):
    return render(request, 'main/main.html')
def about(request):
    return render(request, 'main/about.html')
def fridge(request):
    return render(request, 'main/category_detail.html')
def cupboard(request):
    return render(request, 'main/cupboard.html')
def freezer(request):
    return render(request, 'main/moroz.html')
def news(request):
    return render(request, 'main/fresh_home.html')


def contact(request):
    return render(request, 'main/contact.html')

