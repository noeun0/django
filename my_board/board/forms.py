from django import forms
from .models import Post
#form 클래스 - forms.Form 상속
#ModelForm 클래스 - forms.ModelForm 상속
class PostForm(forms.ModelForm): #화면 쪽을 만드는 것
    # 직접 정의하지 않고, 모델에 있는 것들을 상속 받아서 사용하자.
    # 내부 (NEsted/Inner) 클래스로 Meta 클래스를 정의 -> ModelForm 관련 설정

    class Meta:
        model = Post # form 을 만들때 참조할 Model 클래스 지정
        fields = "__all__" # create_at, update_at 은 auto_now 했기 떄문에 Form Field로 사용안함
        # Model의 Field들 중 Form Field로 만들 Field를 지정. 모두 다 지정할 경우 문자열로 __all__지정
        # 몇몇개만 지정할 경우 리스트에 field이름을 지정한다. ex) fields=['content','title']
        # 특정 Field를 제외한 나머지로 지정할 경우 exclude = ['title'] title 빼고 나머지

        
