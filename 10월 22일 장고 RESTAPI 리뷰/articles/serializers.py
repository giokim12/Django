from rest_framework import serializers #back to anf from front
from .models import Article, Comment #db to and from back

# 게시글 목록
class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title',)

# 댓글 목록
class CommentListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

# 게시글 하나
class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentListSerializer(many =True, read_only = True)

    class Meta:
        model = Article
        fields = '__all__'