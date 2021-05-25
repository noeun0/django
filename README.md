# 프로젝트 만들기

1. django-admin startproject 프로젝트명



2. 프로젝트 디렉토리 생성 후 django-admin startproject 전체설정경로명

   ```
   > mkdir mysite(프로젝트 디렉토리 생성)
   >cd mysite
   >django-admin startproject config .
   ```

   





# App 생성하기

1.  프롬프트 창에서 python manage.py startapp app명 입력

2. **config/settings.py파일의 INSTALLED_APPS에 app명 추가**

3. url 설정 작업

   exam 아래 urls.py 생성

   config/urls.py 에 import include, urlpatterns에 path('exam/', include('exam.urls'))추가

   urls.py(exam)에 from django.urls import path 추가

4. exam/views.py

   사용자 요청을 처리하는 함수 구현

5. exam/urls.py에 위에서 만든 함수와 url을 설정

6. http://127.0.0.1:8000/exam/hello1

url 설정하기

1. 새폴더 생성 exam아래 templates/exam

2. 새파일 : greeting.html

3. html 를 쳐서 자동으로 나오는 html:5 선택


-----

#### 디렉토리

> 파이썬 : 패키지
>
> 장고 : app

config 

- 싸이트에 대한 설정과 관련된 파일이 있는 곳
- settings.py : 전체적인 설정. 리스트,딕셔너리로 이루어져있음. 파이썬으로 설정

PROJECT : 전체 프로젝트

APP : 프로젝트를 구성하는 하위 서비스

