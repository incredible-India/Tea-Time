from django.db import models

# Create your models here.
class QuizStatus(models.Model):
    isEnable  = models.BooleanField(default=False)



class topics(models.Model):
    tname = models.CharField(max_length=250)
    def __str__(self):
        return self.tname


class questions(models.Model):
    topic = models.ForeignKey(topics,on_delete = models.CASCADE)
    question = models.TextField()

    def __str__(self):
        return self.question


class option(models.Model):
    topic = models.ForeignKey(topics,on_delete = models.CASCADE)
    questions = models.ForeignKey(questions, on_delete = models.CASCADE)
    opt1 = models.CharField(max_length=400)
    opt2 = models.CharField(max_length=400)
    opt3 = models.CharField(max_length=400)
    opt4 = models.CharField(max_length=400)
    ans = models.IntegerField()


    
    