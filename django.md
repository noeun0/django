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





---



정적 + 동적 서비스 -> 웹 어플리케이션

동적 서비스를 위해선 웹 어플리케이션 서버가 필요하다. (실행환경)

- 만들때 다양한 언어를 사용할 수 있지만 규약이 필요하고 각각의 실행 환경이 필요하다 -> CGI 
- 장고 : 파이썬으로 웹 어플리케이션을 개발할 수 있는 환경

### MVT패턴

> 역할에 따라 나눠서 개발하자.
>
> -> 유지보수, 재사용성, 확장성, 유연성이 좋아진다.

M : model

- 데이터베이스의 데이터를 다룬다.
- ORM을 이용해 SQL 문 없이 CRUD작업을 처리한다.

V : view ( = controller) - 매니저 같은 역할

- 사용자의 요청을 받아서 응답할때까지의 처리 과정을 담당한다. ( 일 처리 흐름 Work flow)
- Client 가 요청한 작업을 처리하는 흐름을 담당한다.
- 구현 방법은 함수 기반 방식과 클래스 기반 방식 두가지가 있다.

T : template ( = view)

- Client에게 보여지는 부분 (응답화면)의 처리를 담당한다.



### manage.py

python manage.py 명령어

- startapp: 프로젝트에app을새로생성

- makemigrations: 어플리케이션의변경을추적해DB에적용할변경사항을정리한다.

- migrate: makemigrations 로정리된DB 변경내용을Database에적용한다.

- sqlmigrate: 변경사항을DB에적용할때사용한SQL 확인. 

- runserver: 테스트서버를실행한다.

- shell: 장고shell 실행.

- createsuperuser: 관리자계정생성

- changepassword: 계정의비밀번호변경



----

### ORM이란

> object relational mapping - 객체 관계 매핑
>
> sql문 없이 DB작업이 가능해진다.

객체와 관계형 데이터 베이스의 데이터를 자동으로 연결하여 sql문 없이 데이터 베이스 작업(CRUD)를 작성할 수 있다.

![image-20210526234123958](C:\Users\rey\AppData\Roaming\Typora\typora-user-images\image-20210526234123958.png)



장점

- 비지니스로직과 데이터베이스 로직을 분리할 수 있다. 재사용성 유지보수성이 증가한다.
- DBMS에 대한 종속성이 줄어든다.

단점

- DBMS 고유의 기능을 사용할 수 없다.
- DB의 관계가 복잡할 수록 난이도 또한 올라간다.

----



# Model 생성 절차

- 장고 모델을 먼저 만들고 데이터베이스에 적용
  1.  models.py에 model 클래스 작성
  2. admin.py에 등록(admin app에서 관리할 경우)
     - admin.site.register(모델 클래스)
  3. 마이그레이션(migration)파일 생성 - (makemigrations 명령)
     - 변경 사항 db에 넣기 위한 내역을 가진 파일로 app/migrations 디렉토리에 생성된다.
     - python manage.py makemigrations
     - sql문 확인
       - python manage.py sqlmigrate app이름 마이그레이션파일명
  4. Database에 적용(migrate 명령)
     - python manage.py migration

- DB에 테이블이 있을 경우 다음을 이용해 장고 Model 클래스들을 생성할 수 있다.





