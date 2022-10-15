from django.contrib import admin
from .models import QuizStatus,topics,questions,option
@admin.register(QuizStatus)
class QuizstatusAdmin(admin.ModelAdmin):
    list_display = ['id','isEnable']


@admin.register(topics)
class topicsAdmin(admin.ModelAdmin):
    list_display = ['id','tname']


@admin.register(questions)
class topicsAdmin(admin.ModelAdmin):
    list_display = ['id','question','topic']



@admin.register(option)
class topicsAdmin(admin.ModelAdmin):
    list_display = ['id','questions','opt1','opt2','opt3','opt4','ans']
# Register your models here.
