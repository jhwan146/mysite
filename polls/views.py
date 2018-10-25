from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question, Choice
from django.utils import timezone 


def qna(request):
    return render(request, 'polls/qna.html', {})

def add_question(request):
    text = request.POST['text']

    q = Question(
        question_text=text,
        pub_date=timezone.now())
    q.save()
    return HttpResponse('접수되었습니다')

# def add_question(request):
#     text = request.POST['text']
#
#     q = Question(
#         question_text=text,
#         pub_date=timezone.now())
#     q.save()
#     return  HttpResponse('입력 완료')

def data(request, email, number):
    # http: // localhost: 8000 / polls / data?user_name = kim
    value = request.GET['user_name']
    return HttpResponse(value + email + str(number))

def vote(request):
    choice = request.POST['choice']
    c = Choice.objects.get(pk=choice)
    c.votes = c.votes + 1
    c.save()
    print('@@@@@@@@', choice)
    # 정상적으로 작동하면 cmd 서버에 @@@@@@@@@ on
    return render(request, 'polls/vote.html', {})

def detail(request, id):
    question = Question.objects.get(id=id)
    return render(request, 'polls/detail.html', {'item': question})

def index(request):
    list = Question.objects.all()

    # return render(request, ''. {})
    return render(request, 'polls/index.html', {'question': list})

def result(request, id):
    question = Question.objects.get(pk=id)
    return render(request, 'polls/result.html', {'question' : question})