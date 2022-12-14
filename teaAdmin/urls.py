from django.urls import path 
from . import views as v

urlpatterns = [
    path('',v.adminPage.as_view(),name='adminclass'),
    path('see/topic/<int:id>/',v.addQuestion.as_view(),name='question'),
    path('delete/topic/<int:id>/',v.deleteTopic.as_view(),name='adminclass'),
    path('alldelete/topic/<int:passw>/',v.alldelete.as_view(),name='adminclass'),
    path('delete/question/<int:id>/<int:tid>',v.deleteQuestion.as_view(),name='delquestion'),
    path('edit/question/<int:qid>/<int:tid>/<int:oid>/',v.editQuestion.as_view(),name='editquestion'),

]