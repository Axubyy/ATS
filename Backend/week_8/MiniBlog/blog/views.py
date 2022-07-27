from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views import View

from django.urls import reverse

from .forms import CommentForm

from .models import BlogPost, Bloggers, Comment

# Create your views here.


# class CreateCommentView(CreateView):
#     template_name = 'blog/create_comment.html'
#     model = Comment
#     form_class = CommentForm
#     success_url = 'blog/'


class BlogDetailView(DetailView):
    # model = BlogPost
    # template_name = "blog/blog_detail.html"
    # context_object_name = 'blog_post'

    def get(self, request, pk):
        blog_post = BlogPost.objects.get(pk=pk)
        comments = blog_post.comments.all()
        print(comments)
        return render(request, 'blog/blog_detail.html', {
            "blog_post": blog_post,
            "comments": comments,
            "comment_form": CommentForm()

        })

    def post(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            # sets the comment post attribute to this Instance of the blogPost
            comment.post = blog_post
            commenter = comment.user
            comment.save()
            return HttpResponseRedirect(reverse('blog:blog-detail', args=[pk]))

        else:
            return render(request, 'blog/blog_detail.html', {
                "blog_post": blog_post,
                "comment_form": comment_form

            })

    # def get_context_data(self, **kwargs):
    #     context = super(BlogDetailView, self).get_context_data(**kwargs)
    #     context["comment_form"] = CommentForm()
    #     return context


class BlogTemplateView(View):
    template_name = "blog/blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super(BlogTemplateView, self).get_context_data(**kwargs)
        blog_posts = BlogPost.objects.all()
        print(blog_posts)

        context.update(list(blog_posts))

        context["blog_post"] = get_object_or_404(
            BlogPost, pk=self.kwargs["pk"])
        return context


class BlogListView(ListView):
    template_name = 'blog/blog_list.html'
    model = BlogPost
    paginate_by = 5
    ordering = ['post_date']
    context_object_name = 'blog_list'

    def get_queryset(self):
        return super(BlogListView, self).get_queryset()


class BloggersListView(ListView):
    template_name = 'blog/bloggers_list.html'
    model = Bloggers
    context_object_name = 'bloggers_list'


class BloggerDetailView(DetailView):
    template_name = 'blog/blogger_detail.html'
    model = Bloggers
    context_object_name = 'single_blogger'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        single_blogger = get_object_or_404(Bloggers, pk=self.kwargs['pk'])

        context['single_blogger'] = single_blogger
        return context


def home(request):
    blog_posts = BlogPost.objects.all()
    blog_posts_count = blog_posts.count()

    return render(request, 'blog/index.html', {
        "blog_posts": blog_posts,
        "blog_posts_count": blog_posts_count
    })


def index(request):
    blog_posts = BlogPost.objects.all()
    blog_posts_count = blog_posts.count()
    all_bloggers = Bloggers.objects.all().count()

    return render(request, 'index.html', {
        "blog_posts": blog_posts,
        "blog_posts_count": blog_posts_count,
        "all_bloggers": all_bloggers,
    })
