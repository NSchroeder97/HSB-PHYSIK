from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Benutzername', 
                               min_length=4,
                               max_length=150,
                               widget=forms.TextInput(
                                   attrs={'class' : 'form-control'}
                                ),
                               error_messages={'required': 'Benutzername ist schon vergeben!'}
                               )
    email = forms.EmailField(label='E-Mail',widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password1 = forms.CharField(label='Passwort', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(label='Passwort Wiederholung', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
    
    
    
def register(request):
    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
           # user = authenticate(username=username, password=password)
            #login(request, user)
            messages.success(request, 'Account created successfully')
            return redirect('/')
        
        else:
            return render(request, 'main/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'main/register.html',  {'form': form})



def auth_login(request):
    if request.user.is_authenticated:
        return render(request, 'main/index.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Einloggen erfolgreich')
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'main/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'main/login.html', {'form': form})
    
    
    
def signout(request):
    logout(request)
    return redirect('/')