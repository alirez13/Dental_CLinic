from django.http import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from hitcount.views import HitCountDetailView
from .models import *



def blog(request):
    post = Article.objects.all()
    recent_post = Article.objects.all()[:3]

    page_number = request.GET.get('page')

    paginator = Paginator(post, 1)
    obj_list = paginator.get_page(page_number)

    return render(request, 'blog/blog.html', context={'post': obj_list, 'recent_post': recent_post})


class BlogDetail(HitCountDetailView):
    context_object_name = 'post'
    template_name = 'blog/blog-detail.html'
    count_hit = True

    def get_object(self, queryset=None):
        title = self.kwargs.get('title')
        post = get_object_or_404(Article, title=title)
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_post'] = Article.objects.all()[:2]
        return context


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    obj_list = paginator.get_page(page_number)

    recent_post = Article.objects.all()[:2]

    return render(request, 'blog/blog.html', context={'post': obj_list, 'recent_post': recent_post})


def likes(request, title, pk):
    try:
        like = Like.objects.get(article__title=title, user_id=request.user.id)
        like.delete()
        return JsonResponse({'response': 'unliked'})
    except:
        Like.objects.create(article_id=pk, user_id=request.user.id)

        return JsonResponse({'response': 'liked'})
