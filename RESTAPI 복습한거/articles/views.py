from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentListSerializer

# Create your views here.
@api_view(['GET', 'POST']) #  조회랑 작성하겠음
def article_list(request):
    # request를 get 으로 받아왔으면
    if request.method == 'GET': 
        # Article 모델의 list 가져와서 articles 변수에 넣든가 404 error (db to back)
        articles = get_list_or_404(Article)
        # articles변수를 ArticleListSerializer에 이용해서 serializer 변수에 넣기 (back to front)
        # serializer.py 가서 보면은 field에서 title이랑 id만 json으로 바꿀거임
        # 여러개 가져오면은 many = True 써야됨
        serializer = ArticleListSerializer(articles, many = True)
        # serializer 변수 안에있는거 json 으로 바꾼거 return 
        return Response(serializer.data)

    elif request.method == 'POST': #작성
        #내가 작성한 요청 request의 data를 ArticleListSerializer 써서 serializer 변수 담기
        serializer = ArticleListSerializer(data = request.data) #front to back
        # if serializer is not valid, 밑에있는 주석 return Response(serializer.errors... 써야되는데
        # raise_exception = True 쓰면 주석에 있는거 안써도됨
        if serializer.is_valid(raise_exception=True): 
            serializer.save() # back to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'DELETE', 'PUT']) #조회 삭제 수정
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번 글이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        # 수정 페이지에서는 수정하기 전 원래 글이랑 
        # 내가 수정한거 둘다 serializer 변수에 넣음
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data) #수정한거 return
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET']) #댓글 조회
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT']) #댓글 조회 삭제 수정
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentListSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'댓글 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentListSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST']) 
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)