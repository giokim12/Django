from django.shortcuts import render, redirect,get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm
# from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def index(request):
  articles = Article.objects.all()
  context = {
    'articles':articles,
  }

  return render(request, 'articles/index.html', context)


def detail(request, pk):
    #get object or 404:데이터를 조회하지 못하면 404에러를 띄움
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)



@require_http_methods(['GET', 'POST'])
def update(request, pk):
  article = get_object_or_404(Article, pk=pk)
  if request.method == 'POST':
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
      form.save()
      return redirect('article:detail', article.pk )
  else:
    form = ArticleForm(instance=article)

  context = {
    'form':form,
    'article':article,
  }

  return render(request, 'articles/update.html', context)



@require_http_methods(['GET', 'POST'])
def create(request):
    print('------------------------------')
    print(f'request.GET = {request.GET}')
    print(f'request.POST = {request.POST}')
    print('------------------------------')


    # 사용자의 입력 후 요청이 왔을 때
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            # form.save() 는 객체를 반환한다
            article = form.save()
            return redirect('articles:index')
        return redirect('articles:create')
    # 사용자가 처음으로 생성 페이지에 접근했을 때
    else:
        # form 을 만들고
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_POST
def delete(request):
  article = get_object_or_404(Article, pk=pk)
  article.delete()
  return redirect('articles.html')