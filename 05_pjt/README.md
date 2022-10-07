# < pjt5 >

## 부트스트랩
---
## 1
settings.py의 INSTALLED_APPS에 bootstrap5 넣기  
base.html의 맨 위에 {% load bootstrap5 %} 입력  
base.html의 title 위에 {% bootstrap_css %} 입력


## 2
https://stackoverflow.com/questions/10615872/bootstrap-align-input-with-button  
두 줄에 있는 버튼과 폼 태그를 한줄에 넣기

---
---
## delete
---
button에 들어가있는 href요청은 GET 요청인데,  
views.py 에 있는 @require_POST 때문에 delete 함수가 요청을 받지 못한다.  
따라서 form 태그를 사용해서 버튼을 만들어야한다.  
method="POST" 필수


```HTML
  <form action="{% url 'movies:delete' movie.pk %}" method='POST'> 
    {% csrf_token %}
    <input type="submit" class="btn btn-dark" value="Delete">
  </form>
```

---
---
