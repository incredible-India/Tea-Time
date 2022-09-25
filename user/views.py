from django.shortcuts import render
from django.contrib import messages
from django.views import View

# Create your views here.


class home(View):
    def get(self,request):
        return render(request,'user/index.html')





#accoutn create a new
class crtaccount(View):
    def get(self,request):
        return render(request,'user/crt.html')