from django import forms
from .models import Article

#form class
#모델에 없는 값을 입력받고 싶을 때


#모델 폼 클래스
#모델에 있는 값만 입력받고 싶을 때
class ArticleForm(forms.ModelForm):
  #이 클래스를 설명하는 클래스 - meta
  class Meta:
    model = Article
    #사용자의 입력을 원하는 필드 종류
    fields = '__all__'
    #exclude
