from django.shortcuts import render

# Create your views here.
def index(request):
  name = "지오"
  lunches = ['된장전골', '가지덮밥', '오리주물럭']
  word = 'hi hello'
  longword = 'fnia sf np nglanf lbvk baltb va nt aea von a  n v vrna ln tlvabibl volab'
  flag = 0

  context = { 
    'name': name,
    'lunches': lunches,
    'word': word,
    'longword':longword,
    'flag':flag,
  }
  return render(request, 'index.html', context)
  
def inherit(request):
  return render(request, 'inherit.html')

def throw(request):
  return render(request, 'throw.html')
  
def catch(request):
#   raise
# print(request.GET.get('message'))
  message = request.GET.get('message')

  context = {
    'message':message,
  }
  return render(request, 'catch.html', context)


