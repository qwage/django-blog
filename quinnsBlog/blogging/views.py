from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Post
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class StubView(View):
    def get(self, request, *args, **kwargs):
        body = 'Stub View\n\n'
        if args:
            body += 'Args: \n'
            body += '\n'.join([f'\t{item}' for item in args])
        if kwargs:
            body += 'Kwargs:\n'
            body += '\n'.join([f'\t{key}: {value}' for key, value in kwargs.items()])

        return HttpResponse(body, content_type='text/plain')


class PostListView(ListView):
    model = Post
    template_name = 'blogging/list.html'
    queryset = Post.objects.exclude(published_date__exact=None)


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = 'blogging/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'
