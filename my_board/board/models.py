from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
class Category(models.Model): 
    #항상 models.model 을 상속 받자
    # pk 자동 증가 정수 컬럼
    category_code = models.AutoField(primary_key=True)
    # charFiled() 문자열 필드
    category_name = models.CharField(max_length = 200, verbose_name= "글 카테고리") # verbose_name : 화면에 나올때 라벨명

    def __str__(self):
        return f"{self.pk}. {self.category_name}" 

    # 게시물(글)
    # title, content(글내용), create_at(등록일시), update_at(수정일시),writer(글쓴 사람 - 후에 추가.)
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="글제목")
    content=models.TextField(verbose_name="글내용")#TextField:대용량 text
    #null = False(기본) : not null 여부 - False:Not null, True : null 허용컬럼
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name = "글 분류", null = True, blank = True)
    #작성일시. auto_now_add = True(기본값 :Fale) => insert 시점의 일시를 저장하고 그 이후에는 update를 하지 않음
    create_at = models.DateTimeField(verbose_name='작성일시', auto_now_add=True)# 사용자가 입력하지 않아도
    #수정일시. auto_now=True -> insert/update 할 때마다 그 시점의 일시를 저장
    update_at = models.DateTimeField(verbose_name='수정일시', auto_now = True)

    def __str__(self):
        return f"{self.pk}. {self.title}" # 아이디와 타이틀이 나오게 설정.

