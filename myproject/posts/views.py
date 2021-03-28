from django.shortcuts import render
from .models import Posts

def index(request):
    data = Posts.objects.all()
    context = {'data' : data}
    return render(request, 'posts/list.html', context)