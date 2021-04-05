from django.shortcuts import get_object_or_404, render
from .models import Posts

def index(request):
    data = Posts.objects.all()
    context = {'data' : data}
    return render(request, 'posts/list.html', context)

def detail(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    return render(request, 'posts/detail.html', {'post': post})