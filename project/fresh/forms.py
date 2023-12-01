from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, DateInput, Select, ClearableFileInput
from .models import Articles
from django.contrib.auth.forms import AuthenticationForm
from django import forms



class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'date1', 'date', 'category', 'photo']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата изготовления',
                'type': 'date'  # Добавьте это поле, чтобы использовать виджет выбора даты
            }),
            "date1": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата истечения срока годности',
                'type': 'date'  # Добавьте это поле, чтобы использовать виджет выбора даты
            }),
            "category": Select(attrs={
                'class': 'form-control'
            }),
        }

class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
