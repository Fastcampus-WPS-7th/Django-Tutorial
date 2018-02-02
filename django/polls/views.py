from django.http import HttpResponse
from django.shortcuts import render

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
    """
    question_id에 해당하는 Question객체를 템플릿에 전달
        key: "question"
        template: polls/templates/polls/detail.html
    템플릿에서는
    1. 전달받은 question의 question_text를 출력
        {{ question.question_text }}
    2. question이 가진 모든 Choice들을 ul > li로 출력
        {% for choice in question.choice_set.all %}
    :param request:
    :param question_id:
    :return:
    """
    question = Question.objects.get(pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
