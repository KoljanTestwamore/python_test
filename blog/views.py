from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Post

def index(request):
    latest_post_list = Post.objects.order_by('-published_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/index.html', context)

def article(request, post_id):
    return HttpResponse("You're now looking at post: "+ str(post_id))

def create(request):
    if request.method == 'POST': #здесь пост - имя HTTP метода
        post = Post(title = request.POST['title'], text= request.POST['text'])
        post.save()
        return HttpResponseRedirect(reverse('blog:index'))
    else:
        return render(request, 'blog/create.html')