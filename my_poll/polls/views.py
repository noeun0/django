from .models import Question
from .models import Choice
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse # reverse : path설정 이름으로 url문자열을 만들어주는 함수.

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
        return render(request,'polls/error.html', {"error_message" : "없는 질문을 조회했슴미당."})

#투표 처리 - 선택된 choice의 vote 값을 1 증가
#/polls/vote
def vote(request):
    # 요청 파라미터 조회 + 검증
    #post 요청 : request.POST.get('요청파라미터이름') request.POST['이름']
    # 방법1. request.POST.get('요청파라미터 이름')으로 값을 변수에 넣어서 그 변수를 출력해주기 (if문 사용)
    # 방법2. request.POST['이름']와 같은 딕셔너리 형태로 바로 출력 <- 딕셔너리형태로 했을때 값이 없으면 exception (try except)
    #get 요청 : request.GET.get('요청파라미터이름') request.GET['이름']     
    choice_id = request.POST.get('choice')
    #요청 파라미터 검증 : choice로 넘어온 값이 없다면(none) 다시 vote_form으로 이동.
    question_id = request.POST.get('question_id')
    if choice_id == None:
        
        question = Question.objects.get(pk = question_id)
        return render(request, "polls/vote_form.html",
                      {
                          "question":question,
                          "error_message" : "보기를 선택하세요"
                      })
    #print(type(request.POST), choice_id, request.POST['choice'])
    
    #Business logic처리 - 투표처리
    #update할 보기를 조회
    choice = Choice.objects.get(pk=choice_id)
    #vote의 값을 1 증가
    choice.vote+=1
    choice.save()
    #pk가 있는 거면 update, 없는 거면 insert



    #결과 응답         " url 설정 이름",    args =[path 파라미터 에 전달할 값 , ... , ...]
    url_str = reverse("polls:vote_result", args=[question_id])
    print("-------------",url_str)
    return redirect(url_str)
    #return redirect(f"/polls/vote_result/{question_id}")
# 한 문제의 투표 결과를 보여주는 view. polls/vote_result/번호
def vote_result(request,question_id):
    # 조회
    question = Question.objects.get(pk = question_id)
    return render(request,
                  "polls/vote_result.html",
                  {"question":question})