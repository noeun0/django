# 새 플젝 생성하기

> 게시판 만들기





가상환경 선택

> ctrl + shift + p

```
python : select interpreter
```

프로젝트 생성

```
django-admin startproject cofig .
```

기본 앱 설치

```
python.manage.py migrate
```

관리자 계정 만들기 (잊어버리면 똑같은 방법으로 다시 만들어도된다.)

```
python manage.py create superuser
```

> 후에 아이디, 이메일, 비번 입력

app 디렉토리 생성

```
python manangy.py startapp app이름
```



config/settings.py 에 app 이름 등록

```
istalled app=[

'app 이름' 추가하기
]
```



app 디렉토리 안에 urls 파일 생성, 연결

- app 디렉토리 안 urls

```python
from django.urls import path
from django.urls.resolvers import URLPattern


URLPatterns=[

]
```

- config 디렉토리 안 urls

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('board/', include('board.urls')) 추가!
]
```



BASE_DIR/templates 디렉토리 생성

> layout은 기존에 사용했던 것을 사용함.

```python
<!-- root/templates/layout.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{%block title%}제목{%endblock%}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.min.js" integrity="sha384-+YQ4JLhjyBLPDQt//I+STsc9iw4uQqACwlvpslubQzn4u2UU2UFM80nGisd026JF" crossorigin="anonymous"></script>
</head>
<body>
<div class='container'>
    <a href="/admin">관리</a>
    <hr> 
    {%block contents%}{%endblock contents%}
</div>
</body>
</html>
```

home.html 생성



config/settings.py에 dirs에 템플릿 디렉토리 경로 추가하기.

```python
import os # 추가!!!!
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 윗 부분 추가!!!!!
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



config/urls/py에 home.html 의 url 패턴 등록

> 사용자는 무조건 뷰를 불러야 한다. 바로 url 등록 안된다.

```python
urlpatterns = [
    path("", TemplateView.as_view(template_name = 'home.html'), name='home')
]
```







# 게시판 만들기



# board : 모델 클래스 작성 ( board/models.py)

DB 클래스를 만들자. 

게시물의 제목, 내용, 작성일시, 수정일시, 카테고리 등을 담을 post 클래스와,

카테고리의 종류를 담을 category 클래스 두개를 만들어주자. 

이 두 클래스는 models.Model을 상속 받아서 바로 db와 연결할 수 있게 한다.

컬럼 마다 형태가 다르기 때문에, models의 AutoFiled, CharField 등의 형태로 입력 받는다.

또한 post 클래스의 category 컬럼은 category 클래스를 참조한다. 즉 category 클래스 안의 값들만으로 구성될 수 있게 정해논 것이다.



Post 클래스

> - pk : id 자동 증가 점수
>
> - title : ( 입력 )
>
> - content : ( 입력 )
>
> - 등록 일시 ( 입력 안받음) - 자동으로 등록 
>
> - 수정일시 - (입력 안받음) - 자동으로 등록
>
> - 카테고리 : (고정된 값 중 선택 받음) -> 카테고리 테이블을 따로 만들어야 한다. 
>
>   카테고리(부모), board(자식)관계로 참조



Category 클래스

> - code
> - name



### 1. models.py 에서 board, Cagegory 클래스를 생성.

```python
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
```

- null=true는 null을 허용한다는 뜻, null=true 가 아니면 not null 널을 허용하지 않음 (required와 관련- 필수 입력 사항인지 )
- blank=true 빈 문자욜 허용한다는 뜻.

### 2. admin.py에 모델 클래스 들을 등록해야 한다.(admin 페이지에서 관리해주기위해서)

```python
from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Post)
```




### 3. 쿼리 생성, 실제 DB에 등록

```
python manage.py makemigrations
python manage.py migrate
```



### 4. 관리자 모드에서 카테고리 추가하기



> 모델 ( 카테고리, 포스트)을 만들었다.
>
> 이를 db와 연결했다.
>
> form 은 입력 화면과 연결되어서, 입력 받은 것을 처리하는 view에게 넘겨준다.
>
> db와 독립 된 것이 아니라. 폼 필드, 모델 필드가 서로 연결된다. 새로 만들지 말고, 기존 컬럼들 갖고 모델 폼을 만들 수 있다.  -> 상속
>
> 상속받아서 모델 폼을 만들자. 폼을 상속 받아서
>
> 

---







# Model form 만들기



board 카테고리에 forms.py 생성

> forms.ModelForm을 상속하는 PostForm 클래스를 만든다. 
>
> class meta 안에서 어떤 클래스를 참조할지, 어떤 컬럼을 사용할지 정한다.

```python
#forms.py


from django import forms
from .models import Post
#form 클래스 - forms.Form 상속
#ModelForm 클래스 - forms.ModelForm 상속
class PostForm(forms.ModelForm): #화면 쪽을 만드는 것
    # 직접 정의하지 않고, 모델에 있는 것들을 상속 받아서 사용하자.
    # 내부 (NEsted/Inner) 클래스로 Meta 클래스를 정의 -> ModelForm 관련 설정

    class Meta:
        model = Post # form 을 만들때 참조할 Model 클래스 지정
        fields = "__all__" # create_at, update_at 은 auto_now 했기 떄문에 Form Field로 사용안함 (입력이 필요없)
        # Model의 Field들 중 Form Field로 만들 Field를 지정. 모두 다 지정할 경우 문자열로 __all__지정
        # 몇몇개만 지정할 경우 리스트에 field이름을 지정한다. ex) fields=['content','title']
        # 특정 Field를 제외한 나머지로 지정할 경우 exclude = ['title'] title 빼고 나머지

        
```





( 버튼 누르는 것 말고는 대부분 겟 방식)



# View/template 생성하기

> 사용자가 글 등록하기 위해서 입력받을 폼을 요쳥했을 때. 위에서 만든 모델 폼을 갖고 사용자에세 보여줄 역할을 할 view를 만들어야 한다.

1. 글 등록

   View : CreateView 

   - get 요청 :  등록 화면으로 이동

   - post 요청 : 등록 처리 (redirect 방식으로 성공페이지로 이동)

   1. view, urls 등록 , template 구현
   2. templates/board 디렉토리 -> post_create.html, post_detail.html 생성



views.py

> PostCreateView 생성 - 폼을 보내는 역할
>
> 이는 명령을 받았을 때 입력받을 폼을 보내준다. (html)
>
> form_class  는 그 폼의 구성(요청 파라미터)을 뜻한다.
>
> form_class 를 PostForm 로 했다. PostForm 은  바로 전 단계에서 forms.py에서 지정해주었다. ( post 클래스의 모든 것을 쓴다고 했음)

```python
class PostCreateView(CreateView):
    # 입력 양식 화면 template 경로
    template_name = 'board/post_create.html' # render 기능 
     
    # 넘겨주는 객체
    form_class = PostForm #요청파라미터를 처리할 Form을 지정
    
    success_url = reverse_lazy("board:detail") # 등록 처리 후 이동할 경로 -> redirect 방식으로 이동(다시 요청 필요) -> view 의 url을 등록
    
```



post_create.html 생성하기

> 모델 폼을 받아서 보여줄 페이지이다.
>
> post 형식으로 받는다.
>
> {{form.as_p}}를 사용하게 되면 모델 폼을 보기 좋게 한줄씩 정렬(?) 해준다.
>
> 등록 및 초기화 버튼을 생성시킨다.

```python
#post_create.html

{% extends 'layout.html' %}

{% block title %} 글 등록 {%endblock title%}
{%block contents%}
<form method = 'post'>
    {% csrf_token %} # 위조를 막기 위한 토큰 값
    {{form.as_p}} {# 테이블 형태로 만들어준다. #}
    <button type ='submit'> 글 등록 </button>
    <button type="reset">초기화</button>
</form>

{%endblock contents%}
```



url 등록하기

> urls에 as_view 를 사용하여 등록해주어야 한다.
>
> board:create  와 같은 꼴로 뷰 클래스를 사용할 수 있게 됨.

```python
#urls.py

from django.views.generic import TemplateView
from . import views

app_name = 'board'
urlpatterns=[
    path('detail', TemplateView.as_view(template_name = 'board/post_detail.html'), name = 'detail'),# 게시물 상세 페이지
    path('create', views.PostCreateView.as_view(), name = 'create'), # 글 등록 view url
#as view : html 없이 바로 데이터 보낼 수 있게 하는 것...(?)
]
```



---



# django-bootstrap 패키지 사용하기



설치하기

```
pip install django-bootstrap4
```



config/settings.py INSTALLED_APPS에 등록

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'board',
]
```



{{form}} 을 사용하는 template에서 {%load bootstrap4%} # extends 다음에 임포트 해주어야함

{{form}} 대신에 {%bootstrap_form form%} 사용할 것.

```html
{% extends 'layout.html' %}
{% load bootstrap4%}
{% block title %} 글 등록 {%endblock title%}
{%block contents%}
<form method = 'post'>
    {% csrf_token %}
    {% bootstrap_form form %}
    <!-- {{form.as_p}} {# 테이블 형태로 만들어준다. #} -->
    <button type ='submit' class = "btn btn-primary"> 글 등록 </button>
    <button type="reset" class = "btn btn-primary">초기화</button>
</form>

{%endblock contents%}
```

> post 방식으로 create 요청이 들어오면 
>
> 입력한 값이 model form 으로 들어가고 모델이 DB에 save 해준다.
>
> createview 가 post form 안에 각각 컬럼들의 값을 넣은 후, 1. creatview가 값을 검증 한다.
>
> 값이 다 있을 시 알아서2.  save 메소드를 호출해서 save 해준다. (insert/update)
>
> 그리고 응답은 detail로 해준다.
>
> -> 한 주소에서 등록 폼을 주고, 등록 하는 두 기능을 동시에 한다.
>
> 

- django-bootstrap4 검색 후 도큐먼트 들어가서 테그들을 확인 할 수 있다.

----



정상적으로 등록 했을때 입력 된 글이 나오게 하기.

- 글의 id 를 알려주어야 조회해서 보여줄 수 있다.

  path파라미터 값을 받아야 하고,  detailview를 사용한다.

post_detail.html 

