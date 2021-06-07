import django
from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .forms import PostForm
from django.urls import reverse_lazy
# 글 등록
# CreateView 등록 (저장 - insert 처리)
#     get 방식 요청 : 입력 양식 화면으로 이동 (render())
#     post방식 요청 : 입력(등록)처리,
#                    처리 성공 : 성공 페이지로 이동 (redirect)
#                    처리 실패 : 입력양식 화면으로 이동 (render())
class PostCreateView(CreateView):
    # 입력 양식 화면 template 경로
    template_name = 'board/post_create.html' # render 기능 
     
    # 넘겨주는 객체
    form_class = PostForm #요청파라미터를 처리할 Form을 지정
    
    success_url = reverse_lazy("board:detail") # 등록 처리 후 이동할 경로 -> redirect 방식으로 이동(다시 요청 필요) -> view 의 url을 등록

class PostDetailView(DetailView):