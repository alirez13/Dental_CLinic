from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import *
from hitcount.views import HitCountDetailView


def post_dr(request):
    post_t = Post_Tahere.objects.all()
    recent_post = Post_Tahere.objects.all()[:3]

    page_number = request.GET.get('page')

    paginator = Paginator(post_t, 4)
    obj_list = paginator.get_page(page_number)

    return render(request, 'gallery/post_dr.html', context={'post_t': obj_list, 'recent_post': recent_post})


class PostDetailDR(HitCountDetailView):
    context_object_name = 'post_t'
    template_name = 'gallery/post_detail_dr.html'
    count_hit = True

    def get_object(self, queryset=None):
        title = self.kwargs.get('title')
        post = get_object_or_404(Post_Tahere, title=title)
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            if self.request.user.like.filter(post_id=self.object.id, user_id=self.request.user.id).exists():
                context['is_liked'] = True
            else:
                context['is_liked'] = False
        context['recent_post'] = Post_Tahere.objects.all()[:2]  

        return context




def video(request):
    video = Video.objects.all()
    recent_post = Video.objects.all()[:3]

    page_number = request.GET.get('page')

    paginator = Paginator(video, 2)
    obj_list = paginator.get_page(page_number)

    return render(request, 'gallery/video.html', context={'video': obj_list, 'recent_post': recent_post})


class VideoDetail(HitCountDetailView):
    context_object_name = 'video'
    template_name = 'gallery/video_detail.html'
    count_hit = True

    def get_object(self, queryset=None):
        title = self.kwargs.get('title')
        post = get_object_or_404(Video, title=title)
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_post'] = Video.objects.all()[:2]  
        return context


@login_required
def like(request, pk):
    post = get_object_or_404(Post_Tahere, id=pk)
    try:
        like = get_object_or_404(Like, post_id=pk, user_id=request.user.id)
        like.delete()
        return JsonResponse({'result': 'unliked'})
    except:
        Like.objects.create(post_id=pk, user_id=request.user.id)
        return JsonResponse({'result': 'liked'})
    