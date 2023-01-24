from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
  name = 'GIO'
  fruits = ['귤', '딸기', '사과', '바나나', '파인애플']
  hate = ['구아바', '사과' ]

  context = {
    'name': name,
    'fruits': fruits,
    'hate': hate,
  }
  return render(request, 'articles/index.html', context)

def throw(request):
  return(render(request, 'articles/throw.html'))

def catch(request):
  message = request.GET.get('message')
  context = {
      'message': message,
  }
  return render(request, 'articles/catch.html', context)

def main(request):
  articles = Article.objects.all()
  context = {
    'articles': articles,

  }
  return render(request, 'articles/main.html', context)

def new(request):
  return render(request, 'articles/new.html')

def create(request):
  title = request.GET.get('title')
  content = request.POST.get('content')

  # 원하는 방식대로 혹은 정해진 방식대로 데이터를 검증
  # 유효성 검사

  article = Article(title= title, content= content)
  article.save()

  return redirect('articles:main')

def detail(request, pk):
  article = Article.objects.get(pk=pk)
  context = {
    'article': article,
  }
  return render(request, 'articles/detail.html', context)

def delete(request, pk):
  article = Article.objects.get(pk=pk)
  article.delete()
  return redirect('articles:main')

def edit(request, pk):
  article = Article.objects.get(pk=pk)
  context = {
    'article':article,

  }
  return render(request, 'articles/edit.html', context)

def update(request, pk):
  article = Article.objects.get(pk=pk)
  article.title = request.POST.get('title')
  article.content = request.POST.get('content')
  article.save()
  return redirect('articles:detail', article.pk)