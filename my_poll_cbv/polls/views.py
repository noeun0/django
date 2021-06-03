from .models import Question
from .models import Choice
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse # reverse : path설정 이름으로 url문자열을 만들어주는 함수.
from django.views.generic import ListView, View, DetailView
'''
- View 로직 순서 : 
    1. 사용자 입력값에 대한 검증 및 타입변경 
    2. 비즈니스 로직처리 
    3. 결과 응답
'''


# 질문 목록을 보여주는 뷰 
# http://localhost:8000/[앱이름]/[path]
# http://localhost:8000/polls/list --> config/urls.py 매핑해줘야 한다. 


#listView - 모델의 전체 데이터를 조회해서 template에게 전달(paging 기능 제공)
class QuestionListView(ListView):
    model = Question # 전체 데이터를 조회할 모델클래스 지정
    template_name = "polls/list.html" # 응답할 template 경로
    # 조회결과를 템플릿에게 전달- 이름 : '모델클래스명(소문자)_list' , 'object_list'
    # 다른 이름으로 전달할 경우 : context_object_name = "전송할이름"
def list(request): 
    question_list = Question.objects.all().order_by('-pub_date')  
    print(question_list)
    # 어떤 템플릿을 호출할 것인가.
    # templates 을 호출 : render(request, 'templates의경로'[, template 에 전달할 값을 딕셔너리로] )을 사용 
    return render(request, 'polls/list.html', {"question_list" : question_list})



class VoteView(View):
    def get(self, request, *args, **kwargs):
        question_id = kwargs['question_id']
        try:
            question = Question.objects.get(pk = question_id)
            return render(request, "polls/vote_form.html",{"question":question})
        except:
            return render(request, "polls/error.html", {"error_message":"없는 질문을 조회하셨습니다"})

#post 방식 요청 처리

    def post(self, request, *args, **kwargs):
        choice_id = request.POST.get('choice')
        #요청 파라미터 검증 : choice로 넘어온 값이 없다면(none) 다시 vote_form으로 이동.
        question_id = kwargs['question_id'] #path 파라미터값 조회
        if choice_id == None:
    
            question = Question.objects.get(pk = question_id)
            return render(request, "polls/vote_form.html",
                            {
                                "question":question,
                                "error_message" : "보기를 선택하세요"
                            })
        choice = Choice.objects.get(pk=choice_id)
        choice.vote+=1
        choice.save()
        url_str = reverse("polls:vote_result", args=[question_id])
        return redirect(url_str)

    #return redirect(f"/polls/vote_result/{question_id}")
# 한 문제의 투표 결과를 보여주는 view. polls/vote_result/번호

#question 의 id를 받아서 질문 하나를 조회한 후에 템플릿으로 이동
#primary key 값은 path parameter 로 받아야 한다. urls.py에서 path parameter 의 변수명은 <타입 : pk>
class QuestionDetailView(DetailView):
    model = Question # 데이터를 조회할 model 클래스 지정
    template_name = "polls/vote_result.html"



def vote_result(request,question_id):
    # id를 갖고 하나만 조회
    question = Question.objects.get(pk = question_id)
    return render(request, 
                  "polls/vote_result.html",
                  {"question":question})