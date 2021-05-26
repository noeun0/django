# my_poll

vs code 가상환경 잡기

- 명령 팔레트 : control+shift+p => django 가상환경 선택

- 터미널에서 project 생성

  django-admin startproject config .

settings.py

```python
LANGUAGE_CODE = 'ko-KR'
TIME_ZONE = 'Asia/Seoul'
```

기본 app들 관련 table들 생성

```
> python manage.py migrate
```

관리자 계정 생성

```
> python manage.py createsuperuser
id,email,password() /rey, 은영1214
```



app 생성 ( 이름 polls)

```
> python manage.py startapp polls
```

config/settings.py에 app 등록

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
]
```





# Model 구현



polls/models.py 모델 클래스 구현

```python
class Question(models.Model):
    #변수명 : 컬럼명, 값 : filed 객체타입 -> 타입
    question_text = models.CharField(max_length=200)#CharField == NVACHAR
    pub_date = models.DateTimeField(auto_now_add=True) # auto_now_add=True : insert될 대 일시를 자동 등록(insert)

    def __str__(self):
        return self.quest_text
    # 내가 확인하기 편한 값으로 설정하면 관리페이지에서 보기 편하다.

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    vote = models.PositiveIntegerField(default=0)
    question = models.ForeignKey(to=Question,on_delete=models.CASCADE) # 외래키 어떤 테이블의 어떤 컬럼을 참조하는지 알려주어야함
    # to : 참조 Model 클래스 지정
    # on_delete : 부모 테이블의 값이 delete될 경우 처리방식 , CASCADE: 참조하는 자식데이터도 같이 삭제
    def __str__(self):
        return self.choice_text
```



polls/admin.py에 구현한 모델 클래스 들을 등록

```python
from .models import Question,Choice

admin.site.register(Question)
admin.site.register(Choice)
```



model 클래스를 이용해 DB에 테이블 생성

```python
>python manage.py makemigrations # 테이블 생성 sql문 생성
# 어떻게 만들지를 정의하는 것.
#migration 이라는 폴더가 생김. 테이블 어떻게 만들지 정의되어있는 파일이다.
>python manage.py migrate #디비에 테이블 생성
```



서버 실행

http://127.0.0.1:8000/admin

- 데이터 관리할 수 있는 페이지

  ```
  admin.site.register(Question)
  admin.site.register(Choice)
  ```

  -> 위 코드 덕분에 관리할 수 있게 된다.

  ```python
      def __str__(self):
          return self.quest_text
  ```

  -> 위 함수에서 선택한 컬럼값으로 보여진다.