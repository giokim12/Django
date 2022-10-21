# 07_PJT

## __models.py__
### __M:N 관계에서 many to many field의 위치__  
json 의 Actor 파일에는 이 배우가 어떤 영화를 찍었는지를 참조할만한 필드가 존재하지 않는다.  
하지만 Movies 파일에는 이 영화에 어떤 배우가 출연했는지 참조할 수 있는 값들이 value에 배열로 주어져있다.  
따라서 movie 안에 many to many field를 정의해서 서로 참조가 가능하게 해준다.



### __related_name = ''__
https://velog.io/@hj8853/Django-ManyToMany-relatedname  
역참조 대상인 객체를 부르는 이름을 지정하기  
related_name 옵션을 쓰면 뒤에 _id가 붙기때문에 foreignkey 쓸때 주의하기

---
## __serializers.py__
### __방법1__
```html
class ActorSerializer(serializers.ModelSerializer):
    #배우가 찍은 영화만 가져오기
    class ActorShootMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title', )
            
    movies = ActorShootMovieSerializer(many = True, read_only=True)
    class Meta:
        model = Actor
        fields = ('id', 'movies', 'name', )
```

### __방법 2__

```html

#배우가 찍은 영화만 가져오기
class ActorShootMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', )
            
class ActorSerializer(serializers.ModelSerializer):
    movies = ActorShootMovieSerializer(many = True, read_only=True)
    class Meta:
        model = Actor
        fields = ('id', 'movies', 'name', )
```
얘는 순서에 유의해야한다!!

---
## __views.py__
### @api_view(['GET']) 
get이 왔을때만 이 함수를 동작시키겠다


