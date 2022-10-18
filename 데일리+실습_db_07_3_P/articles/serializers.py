from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title',)


class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    # 2가지 방법
    # 1. primary key related field -> 오버라이딩 하는 방법
    # comments = serializers.PrimaryKeyRelatedField(many = True, read_only=True)
    # 2. nested relationships
    comments = CommentSerializer(many = True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only = True)
    class Meta:
        model = Article
        fields = '__all__'   


# class CommentSerializer(serializers.ModelsSerializer):

#     class Meta:
#         model = Comment
#         fields = '__all__'