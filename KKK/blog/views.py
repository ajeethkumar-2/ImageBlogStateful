from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import *
from .models import *


def Like(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post', args=[str(pk)]))


class Home(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


def Categories(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


class DetailedPost(DetailView):
    model = Post
    template_name = 'detail_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DetailedPost, self).get_context_data(*args, **kwargs)

        post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post.total_likes()

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['cat_menu'] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPost, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class AddCategory(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategory, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePost, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePost, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class AddComment(CreateView):
    model = PostComments
    form_class = CommentForm
    template_name = 'add_comment.html'

    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)