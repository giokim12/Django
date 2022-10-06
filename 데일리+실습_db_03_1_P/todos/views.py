from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_http_methods, require_GET


# Create your views here.
@require_GET
def index(request):
  todos = Todo.object.all()
  context = {
    'todos': todos,
  }
  return render(request, 'todos/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
  if request.method == 'POST':
    form = TodoForm(request.POST)
    if form.is_valid():
      todo = form.save(commit=False)
      todo.author = request.user
      todo.save()
      return redirect('todos:index')
  else:
    form = TodoForm()
  context = {
    'form': form,
  }
  return render(request, 'todos/create.html', context)


@require_POST
def toggle(request, pk):
  if request.
    todo = Todo.objects.get(pk = pk)
    if todo.completed is True:
      todo.completed = False
    else:
      todo.completed = True
    todo.save()
    return redirect('todos:index')
  else:
    return redirect('accounts:login')

@require_POST
def delete(request, pk):
  if request.
    todo = Todo.objects.get(pk = pk)
    if todo.completed is True:
      todo.completed = False
    else:
      todo.completed = True
    todo.save()
    return redirect('todos:index')
  else:
    return redirect('accounts:login') 



