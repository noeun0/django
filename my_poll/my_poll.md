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

