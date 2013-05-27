# Create your views here.
from models import Post
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from forms import PostForm

#def post_list(request):
#    posts = Post.objects.all()
#    context = {'posts': posts}
#    return render_to_response("blog/list.html", context)
#
#def post_detail(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    context = {'post': post}
#    return render_to_response("blog/detail.html", context)

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post
    form_class = PostForm

class PostEdit(UpdateView):
    model = Post
    form_class = PostForm

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
