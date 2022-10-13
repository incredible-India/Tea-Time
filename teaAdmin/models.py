from django.db import models

# Create your models here.
class QuizStatus(models.Model):
    isEnable  = models.BooleanField(default=False)



class topics(models.Model):
    tname = models.CharField(max_length=250)
    
    