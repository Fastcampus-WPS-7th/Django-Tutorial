from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Question


def index(request):
    # 가장 최근에 발행된 최대 5개의 Question목록
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }

    # render를 사용
    return render(request, 'polls/index.html', context)

    # template을 명시적으로 불러와 rendering
    # template = loader.get_template('poll/index.html')
    # return HttpResponse(template.render(context, request))

    # 쉼표단위로 구분된 Question목록의
    #   각 항목의 question_text로 만들어진 문자열을 리턴
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
