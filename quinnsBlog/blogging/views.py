from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from .models import Post
from django.template import loader


def stub_view(request, *args, **kwargs):
    body = 'Stub View\n\n'
    if args:
        body += 'Args: \n'
        body += '\n'.join([f'\t{item}' for item in args])
    if kwargs:
        body += 'Kwargs:\n'
        body += '\n'.join([f'\t{key}: {value}' for key, value in kwargs.items()])

    return HttpResponse(body, content_type='text/plain')


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}

    return render(request, 'blogging/list.html', context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)
