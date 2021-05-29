from .models import Question, Choice
from django.shortcuts import render, redirect
from django.http import HttpResponse

'''
- View 로직 순서 : 
    1. 사용자 입력값에 대한 검증 및 타입변경 
    2. 비즈니스 로직처리 
    3. 결과 응답
'''
# 질문 목록을 보여주는 뷰 
# http://localhost:8000/[앱이름]/[path]
# http://localhost:8000/polls/list --> config/urls.py 매핑해줘야 한다. 
def list(request): 
    question_list = Question.objects.all().order_by('-pub_date')
    print(question_list)
    # 어떤 템플릿을 호출할 것인가.
    # templates 을 호출 : render(request, 'templates의경로'[, template 에 전달할 값을 딕셔너리로] )을 사용 
    return render(request, 'polls/list.html', {"question_list" : question_list})

def vote_form(request, question_id):
    print('vote_form', question_id)
    #question_id 질문 조회
    try:
        question = Question.objects.get(pk = question_id) # filter : 쿼리셋으로 반환.
        return render(request,"polls/vote_form.html",{"question":question}) # templates에서 찾기 시작함
    except:
        return render(request,'polls/error.html')