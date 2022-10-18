from rest_framework import serializers
from .models import Article


# 리스트 출력, create
class ArticleListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = ' __all__'




# detail, update, delete
class ArticleSerializer():
  pass