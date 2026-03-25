from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from dataApp.models import Post

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )

    return render(request, 'hello.html')