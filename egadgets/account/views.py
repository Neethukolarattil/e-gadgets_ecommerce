from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import *
from .forms import RegisterForm,LogForm
from django.views.generic import CreateView,TemplateView,FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

# class LandingView(View):
#     def get(self,request):
#       return render(request,"index.html")

class LandingView(TemplateView):
    template_name="index.html"
    
# class LoginView(View):
#    def get(self,request):
#       return render(request,"log.html")

class LoginView(FormView):
   template_name="log.html"
   form_class=LogForm
   def post(self,request):
      form_data=LogForm(data=request.POST)
      if form_data.is_valid():
         uname=form_data.cleaned_data.get("username")
         pswd=form_data.cleaned_data.get("password")
         user=authenticate(request,username=uname,password=pswd)
         if user:
            print(user)
            login(request,user)
            messages.success(request,"Login successfully")
            return redirect("chome")
         else:
            # print(user,"login failed")
            messages.error(request,"invalid username/password")
            return redirect('log')
      return render(request,'log.html',{"form":form_data})

# class RegView(View):
#    form_class=RegisterForm
#    def get(self,request):
#       form=RegisterForm()
#       return render(request,"reg.html",{"form":form})
#    def post(self,request):
#       form_data=self.form_class(data=request.POST)
#       if form_data.is_valid():
#          form_data.save()
#          return redirect('log')
#       return render(request,"reg.html",{"form":form_data})

class RegView(CreateView):
   form_class=RegisterForm
   template_name="reg.html"
   success_url=reverse_lazy("log")
   def form_valid(self, form: BaseModelForm):
      messages.success(self.request,"Registration completed")
      return super().form_valid(form)
   def form_invalid(self, form: BaseModelForm):
      messages.error(self.request,"Registration Failed")
      return super().form_invalid(form)
   
class LogoutView(View):
   def get(self,request):
      logout(request)
      return redirect("landing")
