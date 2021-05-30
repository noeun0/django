# urls.py 는 url와 view를 연결(매핑)해준다 
# polls/urls.py : polls 앱용 url pattern 설정 스크립트 
# config/urls.py 와 등록해줘야 한다 . 

from django.urls import path
from . import views
#url pattern 들의 namespace(prefix)로 사용할 값 설정
#url pattern 설정의 이름 호출 시 다른 app들과 구분하기 위해 사용한다.

app_name = "polls"
urlpatterns = [
    path('list', views.list, name='list'),
    path('vote_form/<int:question_id>', views.vote_form, name = 'vote_form'), #vote_form/1 이런식으로 url 
    path('vote', views.vote, name='vote'),
    path('vote_result/<int:question_id>', views.vote_result, name='vote_result'),
]
