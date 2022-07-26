from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView

from .models import BlogPost

# Create your views here.


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blog_detail.html"

    def get_context_data(self, **kwargs):
        return super(BlogDetailView, self).get_context_data(**kwargs)


class BlogTemplateView(TemplateView):
    template_name = "blog/blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super(BlogTemplateView, self).get_context_data(**kwargs)
        # blog_posts = BlogPost.objects.all()
        # print(blog_posts)

        # context.update(list(blog_posts))

        context["blog_post"] = get_object_or_404(
            BlogPost, pk=self.kwargs["pk"])
        return context


class BlogView():
    pass


def home(request):
    blog_posts = BlogPost.objects.all()
    blog_posts_count = blog_posts.count()

    return render(request, 'blog/home.html', {
        "blog_posts": blog_posts,
        "blog_posts_count": blog_posts_count
    })
