from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.views import View
from .models import QuizStatus,topics
# Create your views here.


class adminPage(View):
    def get(self, request):

        isEnable = QuizStatus.objects.all()


        if isEnable.exists() == False:
           isEnable= QuizStatus.objects.create(isEnable=False).save()


        #for the topics  

        topic = topics.objects.all()





        

        return render(request, 'teaAdmin/admin.html',{
            'isEnableDBS': isEnable,
            'topic': topic,
            'tl': len(topic)
        })

    def post(self,request):

        name = request.POST.get('topic')

        if name.strip() == '':
            messages.error(request,'Please enter the topic name..')
            return HttpResponseRedirect('/controlroom')

        isExist = topics.objects.filter(tname=name).exists()

        if isExist:
            messages.info(request,'Topic Name  Already Exist..')
            return HttpResponseRedirect('/controlroom')

        else:
            topics.objects.create(tname=name).save() 
            

        return HttpResponseRedirect('/controlroom')




#for deleting the topics.. 
class deleteTopic(View):
    def get(self, request,id):

        isExist = topics.objects.filter(id=id)


        if isExist.exists():
            topics.objects.get(id=id).delete()
            return HttpResponseRedirect('/controlroom')
        else:
            return HttpResponse('<h1>invalid topic.. </h1>')

