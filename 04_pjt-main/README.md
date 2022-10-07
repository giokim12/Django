# PROJECT 04

## 시작
___

```html
python -m venv venv
source venv/Scripts/activate
pip install django==3.2.13
django-admin stratproject <내프로젝트이름> #이 프로젝트는 mypjt
python manage.py runserver
python managy.py startapp <앱이름> #이 프로젝트에서는 movies
```
templates폴더  
templates안에 movies 폴더  
그 안에 만들 html들 만들기  
movies 안에 urls.py 만들기  
제일 바깥에 inherit 폴더 만들고 그 안에 base.html 만들기  
base.html 안에 !+tab  

## 데이터 불러오기
----

movies 폴더 안에 models.py 안에 
```html
class Movie(models.Model):
  title = models.CharField(max_length=20)
  ...
```
주어진 클래스 경로 형식 넣기

```html
python manage.py makemigrations
```
migration 파일 만들어진거 확인
```html
python manage.py migrate
```
-----
## new
```html
from django.contrib import admin
from django.urls import path,include
from . import views
```
url.py 쓸때 
```html
path('new/', views.new, name='new'),
```
**뒤에 꼭 / 쓰기!!!!**

views.py 쓸 때
```html
def create(request):
  title = request.POST.get('title')
```
**POST 쓰기!!** GET XX

그리고 마지막에 redirect>> index 가게 만들기  
이거하면 영화데이터가 db에 올라감

이후, 맨 밑에있는 db.sqlite3 우클릭해서 opendatabase로 확인

----
## index

주소가 movies 일때 index 출력하는거니까
```
app_name="movies"
urlpatterns = [
  path('', views.index, name="index"),
```

영화 하나 하나씩 출력하는거니까 for문 쓰기  

```
<a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a>
```

____

## detail
**views.py에서 마지막에 context 쓰는거 잊지말기**

----

## edit
db불러올때 텍스트 말고 다른거 불러오기
```
      <label for="release_date">RELEASE_DATE</label>
      <input type="date" name="release_date" id="release_date" value= "{{ movie.release_date|date:"Y-m-d" }}">
      <br>
      <label for="genre" class="form-label">GENRE</label>
        <select class="form-select" name="genre" form="update">
          {% for i in genres %}
            {% if i == movie.genre %}
              <option value="{{ movie.genre }}" selected>{{ movie.genre }}</option>
            {% else %}
              <option value="{{ i }}">{{ i }}</option>
            {% endif %}
          {% endfor %}
        </select>
```
날짜 타입: value 뒤에 |date:'Y-m-d'로 형식 지정해주기  
영화 장르 select: for문이랑 if 문 써서 입력값이랑 장르랑 이름 똑같으면 장르 출력, 아니면 입력값 출력

---
## admin

```
python manage.py createsuperuser
```