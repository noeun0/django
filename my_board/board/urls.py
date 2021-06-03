from board.views import PostCreateView
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'board'
urlpatterns=[
    path('detail', TemplateView.as_view(template_name = 'board/post_detail.html'), name = 'detail'),# 게시물 상세 페이지
    path('create', views.PostCreateView.as_view(), name = 'create'), # 글 등록 view url
#as view : html 없이 바로 데이터 보낼 수 있게 하는 것...
]