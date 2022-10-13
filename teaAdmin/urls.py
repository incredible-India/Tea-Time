from django.urls import path 
from . import views as v

urlpatterns = [
    path('',v.adminPage.as_view(),name='adminclass'),
    path('delete/topic/<int:id>/',v.deleteTopic.as_view(),name='adminclass'),
    path('alldelete/topic/<int:passw>/',v.alldelete.as_view(),name='adminclass'),
]