
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views import View
from django.views.generic.edit import CreateView
from .forms import *
from .models import *
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class Home(View):

    def get(self,request):

        return render(request,'hospital_main/home.html')
    
def LoginView(request):


	if request.method == 'POST':

		nick = request.POST.get('log')
		passw = request.POST.get('pass')

		user = authenticate(request,username=nick,password=passw)

		if user is not None:

			login(request, user)

			return redirect('hospital_main:home')


	return render(request,'hospital_main/login.html')
    
def RegisterView(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('hospital_main:login')
    return render(request,'hospital_main/register.html',{'form':form})

class Logout(View):
   template_name = 'hospital_main\logout.html'
   success_url = reverse_lazy('hospital_main:login')
   def get(self,request):
       return render(request,self.template_name)
   def post(self,request):
       if request.user.is_authenticated:
            logout(request)
            return redirect(reverse_lazy('hospital_main:login'))
       else:
        return render(request,self.template_name)