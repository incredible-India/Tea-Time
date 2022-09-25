from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from django.views import View
from .models import user
from .middleware import istrusted
from django.utils.decorators import method_decorator
from django.db.models import Q

# Create your views here.


class home(View):
    @method_decorator(istrusted)
    def get(self,request):
        if request.isauth :
            return render(request,'user/index.html',{'uname' : request.name})
        else:
            return render(request,'user/index.html')





#accoutn create a new
class crtaccount(View):

    @method_decorator(istrusted)
    def get(self,request):
        if request.isauth == False:
            return render(request,'user/crt.html')
        else:
            return HttpResponseRedirect('/')
    
    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        upi = request.POST.get('upi')
        password = request.POST.get('password')


        if name.strip() == ''  or len(name.strip()) <= 2:
            messages.info(request,'Name Should not be blank or it should be greater than 3 characters')
            return HttpResponseRedirect('/create/account/')
        elif email.strip() == '' or len(email.strip()) <= 12:
            messages.info(request,'incorrect email address')
            return HttpResponseRedirect('/create/account/')
        elif password.strip() == '' or len(password.strip()) <= 5 :
            messages.info(request,'Password is too small it should be at least 6 characters')
            return HttpResponseRedirect('/create/account/')
        

        isexist  =  user.objects.filter(email = email).exists()

        if isexist:
            messages.info(request,'Email already exists please try another one or go for login.')
            return HttpResponseRedirect('/create/account/')

        if len(upi.strip()) == 0  :
            upi = False

        
        user.objects.create(name=name , email=email, password=password,upi=upi)

        request.session['name'] = name 
        request.session['email'] = email

        return HttpResponseRedirect('/')


        


#login login
class login(View):
    @method_decorator(istrusted)
    def get(self,request):
        if request.isauth == False:
            return render(request,'user/login.html')
        else:
            return HttpResponseRedirect('/')
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email.strip() == '':
            messages.info(request,'Email should not be blank..')
            return HttpResponseRedirect('/login')
        elif password.strip() == '':
            messages.info(request,'Password should not be blank..')
            return HttpResponseRedirect('/login')
        
        else:
            isexist = user.objects.filter(Q(email=email) & Q(password=password)).exists()
            

            if isexist:
                name = user.objects.get(email=email).name
                request.session['name'] = name 
                request.session['email'] = email
                return HttpResponseRedirect('/')
            else:
                messages.info(request,'Invalid credential..')
                return HttpResponseRedirect('/login')


class logout(View):
    @method_decorator(istrusted)
    def get(self,request):
        if request.isauth :
            del request.session['name']
            del request.session['email']
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')



 