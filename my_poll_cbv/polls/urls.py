# urls.py 는 url와 view를 연결(매핑)해준다 
# polls/urls.py : polls 앱용 url pattern 설정 스크립트 
# config/urls.py 와 등록해줘야 한다 . 

from django.urls import path
from . import views
from . models import Question
from django.views.generic import ListView, DetailView
#url pattern 들의 namespace(prefix)로 사용할 값 설정
#url pattern 설정의 이름 호출 시 다른 app들과 구분하기 위해 사용한다.

app_name = "polls"
urlpatterns = [
    #클래스 기반 뷰를 등록 : 이름.as_view()를 붙혀주어야한다.
    #path('list', views.QuestionListView.as_view(), name='list'),
    path("list", ListView.as_view(model = Question, template_name = "polls/list.html"),name = 'list'),
    path('forms/<int:question_id>', views.VoteView.as_view(), name = 'vote'), #vote_form/1 이런식으로 url 
    #path('vote', views.vote, name='vote'),
    #path('result/<int:pk>', views.QuestionDetailView.as_view(), name='vote_result'),
    path('reult/<int:pk>', DetailView.as_view(model = Question, template_name = 'polls/vote_result.html'), name = 'vote_result'),
]
