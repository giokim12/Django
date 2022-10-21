from rest_framework import serializers #back to and from front
from .models import Actor, Movie, Review #db to and from back


#전체 배우
class ActorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', )

#전체 영화
class MoviesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview', )

#전체 리뷰
class ReviewsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content', )

# #배우가 찍은 영화만 가져오기
# class ActorShootMovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ('title', )

#영화에 해당하는 배우들 이름만 가져오기
class MovieParticipateActors(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name', )

#단일 배우
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

#해당 영화에 맞는 리뷰 출력
class MoviesReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content', )

#단일 영화
class MovieSerializer(serializers.ModelSerializer):
    actors = MovieParticipateActors(many = True, read_only=True)
    review_set = MoviesReviewSerializer(many = True, read_only = True)
    class Meta:
        model = Movie
        fields = '__all__'


#해당 리뷰에 맞는 영화
class ReviewsMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', )
#단일 리뷰
class ReviewSerializer(serializers.ModelSerializer):
    movie = ReviewsMovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'




