from django.shortcuts import render, get_object_or_404
from .models import Post
# O ponto antes de models significa diretório atual ou aplicativo atual.
from django.utils import timezone


# request (tudo o que recebemos do usuário através da Internet)
def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
