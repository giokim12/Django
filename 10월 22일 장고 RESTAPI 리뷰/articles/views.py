from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentListSerializer

# Create your views here.
@api_view(['GET'])
def article_list(request):
    pass
    

def article_detail(request, article_pk):
    pass

def comment_list(request):
    pass

def comment_detail(request, comment_pk):
    pass

def comment_create(request, article_pk):
    pass