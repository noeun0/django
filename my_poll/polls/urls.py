# urls.py 는 url와 view를 연결(매핑)해준다 
# polls/urls.py : polls 앱용 url pattern 설정 스크립트 
# config/urls.py 와 등록해줘야 한다 . 

from django.urls import path
from . import views

urlpatterns = [
    path('list', views.list, name='list'),
    path('vote_form/<int:question_id>', views.vote_form, name = 'vote_form'), #vote_form/1 이런식으로 url 
    path('vote', views.vote, name='vote'),
    path('vote_result/<int:question_id>', views.vote_result, name='vote_result'),
]