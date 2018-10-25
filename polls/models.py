from django.db import models

from django.db import models

# Ctrl + Alt + l = 정렬

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text              #override - 터미널에서 print() 하면 내용이 직접 출력됨

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text + ' // ' + str(self.votes)

# Question 과 Choice 외래키로 연결되어 있음