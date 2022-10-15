from http.client import HTTPResponse
from xml.dom.xmlbuilder import Options
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.views import View
from .models import QuizStatus, questions,topics,option
from django.db.models import Q

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


class alldelete(View):
    def get(self, requests,passw):
        

        if passw != 123456:
            return HttpResponse('kuchh to gadbad hai daya')

        data = topics.objects.all()
        if data.exists():
            data.delete()
            return HttpResponseRedirect('/controlroom')
        else:
            return HttpResponse('kuchh to gadbad hai daya')




#todo for adding the question to the selected topics 

class addQuestion(View):
    def get(self, request,id):

        topicname = topics.objects.filter(id=id) 



        if topicname.exists():

            quest = questions.objects.filter(topic = topics.objects.get(id=id))

            opt = option.objects.filter(topic = topics.objects.get(id=id) )
            return render(request,'teaAdmin/question.html',{'topicname':topicname
            ,'quest':quest,'opt':opt,'total' : len(quest)})

            
        else:
            return HttpResponse('<h1> Something went wrong </h1>')
        
    def post(self,request,id):
        
        quest = request.POST.get('question')
        opt1 = request.POST.get('opt1')
        opt2 = request.POST.get('opt2')
        opt3 = request.POST.get('opt3')
        opt4 = request.POST.get('opt4')
        ans = request.POST.get('ans')

        if len(quest.strip()) < 9:
            messages.error(request,'Question Should not be blank or less than 10 characters..')
            return HttpResponseRedirect(f'/controlroom/see/topic/{id}')
        if len(opt1.strip()) < 1:
            messages.error(request,'option 1 Should not be blank or less than 1 characters..')
            return HttpResponseRedirect(f'/controlroom/see/topic/{id}')
        if len(opt2.strip()) < 1:
            messages.error(request,'Option 2 Should not be blank or less than 1 characters..')
            return HttpResponseRedirect(f'/controlroom/see/topic/{id}')
        if len(opt3.strip()) < 1:
            messages.error(request,'Option 3 Should not be blank or less than 1 characters..')
            return HttpResponseRedirect(f'/controlroom/see/topic/{id}')
        if len(opt4.strip()) < 1:
            messages.error(request,'Option 4 Should not be blank or less than 1 characters..')
            return HttpResponseRedirect(f'/controlroom/see/topic/{id}')

        
        que =  questions.objects.filter(Q(question = quest) & Q(topic=topics.objects.get(id=id)))

        if que.exists():
            messages.error(request,'Question Already Exist..')
            return HttpResponseRedirect(f'/controlroom/see/topic/{id}')
        else:
            #question save the first
            questions.objects.create(question=quest, topic = topics.objects.get(id=id)).save()
            #now save the options 
            
            option.objects.create(questions=questions.objects.get(question=quest), topic = topics.objects.get(id=id),opt1=opt1, opt2=opt2,opt3=opt3, opt4=opt4,ans=ans).save()
            return HttpResponseRedirect(f'/controlroom/see/topic/{id}')






#deleting the questions 

class deleteQuestion(View):
    def get(self, request,id,tid):
        isExist = questions.objects.filter(Q(id=id) & Q(topic = topics.objects.get(id=tid)))

        if isExist.exists():
            isExist.delete()
            return HttpResponseRedirect(f'/controlroom/see/topic/{tid}')

        else:
            return HttpResponse('<Kuchh to gadbad hai daya</h1>')


class editQuestion(View):
    def get(self, request,qid,tid,oid):
        #checking the database ...
        isExist = questions.objects.filter(Q(id=qid) & Q(topic = topics.objects.get(id=tid)))

        if isExist.exists():
            isopt = option.objects.filter(Q(id=oid) & Q(topic = topics.objects.get(id=tid)) & Q(questions = questions.objects.get(id=qid)))

            if isopt.exists():
                return render(request, 'teaAdmin/edit.html',{
                    'qt':isExist, 'opt' :isopt
                })
            else:
                return HttpResponse('Again kuchh to gadbad hai')
        else:
            return HttpResponse('Gadbad hai bhai, kuchh to gadbad hai')
    

    def post(self,request,qid,tid,oid):

        quest = request.POST.get('quest')
        opt1 = request.POST.get('opt1')
        opt2 = request.POST.get('opt2')
        opt3 = request.POST.get('opt3')
        opt4 = request.POST.get('opt4')
        ans = request.POST.get('ans')
        isExist = questions.objects.filter(Q(id=qid) & Q(topic = topics.objects.get(id=tid)))

        if isExist.exists():
            isopt = option.objects.filter(Q(id=oid) & Q(topic = topics.objects.get(id=tid)) & Q(questions = questions.objects.get(id=qid)))

            if isopt.exists():
                isExist.update(question = quest)
                isopt.update(opt1=opt1,opt2=opt2,opt3=opt3,opt4=opt4,ans=ans)

                messages.success(request,'Question Updated successfully..')

                return HttpResponseRedirect(f'/controlroom/edit/question/{qid}/{tid}/{oid}/')
            else:
                return HttpResponse('Again kuchh to gadbad hai')
        else:
            return HttpResponse('Gadbad hai bhai, kuchh to gadbad hai')
