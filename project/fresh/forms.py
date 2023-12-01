from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, DateInput, Select, ClearableFileInput
from .models import Articles
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from datetime import datetime



class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'date1', 'date', 'category', 'photo']

        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "date": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            "date1": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            "category": forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        date1 = cleaned_data.get('date1')

        if date and date1:
            # Преобразование строковых значений дат в объекты datetime
            date = datetime.strptime(str(date), '%Y-%m-%d').date()
            date1 = datetime.strptime(str(date1), '%Y-%m-%d').date()

            if date > date1:
                self.add_error('date', 'Дата изготовления не может быть больше даты истечения срока годности')
                self.add_error('date1', 'Дата изготовления не может быть больше даты истечения срока годности')

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        date1 = cleaned_data.get('date1')

        if date and date1 and date > date1:
            self.add_error('date', 'Дата изготовления не может быть больше даты истечения срока годности')
            self.add_error('date1', 'Дата изготовления не может быть больше даты истечения срока годности')
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
