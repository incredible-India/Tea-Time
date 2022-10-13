from django.contrib import admin
from .models import QuizStatus,topics
@admin.register(QuizStatus)
class QuizstatusAdmin(admin.ModelAdmin):
    list_display = ['id','isEnable']


@admin.register(topics)
class topicsAdmin(admin.ModelAdmin):
    list_display = ['id','tname']
# Register your models here.
