from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core import serializers
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer



# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                # 'created_at': article.created_at,
                # 'updated_at': article.updated_at,
            }
        )
    return JsonResponse(articles_json, safe=False)


def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles, fields=('title', 'content',))
    return HttpResponse(data, content_type='application/json')

@api_view(['GET'])
def article_json_3(request):
    article = Article.objects.all()
    serializer = ArticleListSerializer(articles, many = True)
    return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        # articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    articles = Article.objects.get(pk=article_pk)
    # article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        message = {
            'delete': f'데이터 {article_pk}번 글이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)