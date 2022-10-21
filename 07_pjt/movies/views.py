from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Actor, Movie, Review
from .serializers import *
# from .serializers import ActorsListSerializer, ActorSerializer, ActorShootMovieSerializer, MoviesListSerializer, MovieSerializer, ReviewSerializer

# Create your views here.

#전체 배우
#단일 배우
#전체 영화
#단일 영화
#전체 리뷰
#단일 리뷰 조회 수정 삭제
#리뷰 생성


#전체 배우 조회만 하는거 
@api_view(['GET']) #get이 왔을때만 이 함수를 동작시키겠다
def actor_list(request):
    # if request.method == 'GET':
    actors = get_list_or_404(Actor)
    serializer = ActorsListSerializer(actors, many = True)
    return Response(serializer.data)

#단일 배우 조회만 하는거
@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk = actor_pk )
    serializer = ActorSerializer(actor)
    return Response(serializer.data)


#전체 영화 조회만 하는거 
@api_view(['GET'])
def movie_list(requset):
    movies = get_list_or_404(Movie)
    serializer = MoviesListSerializer(movies, many = True)
    return Response(serializer.data)


#단일 영화 조회만 하는거
@api_view(['GET'])
def movie_detail(requset, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


#전체리뷰
@api_view(['GET'])
def review_list(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewsListSerializer(reviews, many = True)
    return Response(serializer.data)



#리뷰 조회 수정 삭제
@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'review {review_pk} is deleted'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 리뷰 작성
@api_view(['POST'])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)