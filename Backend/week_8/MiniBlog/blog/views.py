from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView


from django.urls import reverse, reverse_lazy

from .forms import BlogPostCreateForm, CommentForm, ProfileForm, UserUpdateForm

from .models import BlogPost, Bloggers, Comment, Profile, User

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
        liked = False
        blog_post = BlogPost.objects.get(pk=pk)
        comments = blog_post.comments.filter(
            is_deleted=False, post=blog_post).order_by('-post_date')

        # blog_post = get_object_or_404(
        #     BlogPost, pk=post_id)
        total_likes = blog_post.total_likes()
        if request.user.is_authenticated:
            if blog_post.likes.filter(id=request.user.id).exists():
                blog_post.likes.remove(request.user)
                liked = False
            else:
                blog_post.likes.add(request.user)
                liked = True
        else:
            pass
        post_likers = blog_post.likes.all()
        return render(request, 'blog/blog_detail.html', {
            "blog_post": blog_post,
            "total_likes": total_likes,
            "liked": liked,
            "post_likers": post_likers,
            "comments": comments,
            "comment_form": CommentForm()

        })

    # def post(self, request, pk):
    #     blog_post = get_object_or_404(BlogPost, pk=pk)
    #     comment_form = CommentForm(request.POST)
    #     if comment_form.is_valid():
    #         comment = comment_form.save(commit=False)
    #         # sets the comment post attribute to this Instance of the blogPost
    #         comment.post = blog_post
    #         comment.user = request.user
    #         comment.save()
    #         return HttpResponseRedirect(reverse('blog:blog-detail', args=[pk]))

    #     else:
    #         return render(request, 'blog/blog_detail.html', {
    #             "blog_post": blog_post,
    #             "comment_form": comment_form

    #         })

    def post(self, request, pk):
        blog_post = BlogPost.objects.get(pk=pk)
        resp = {}
        if blog_post:
            comment_form = CommentForm(request.POST)
            comment = request.POST.get("comment", '')
            # comment = request.POST.get("description", None)
            print(comment)
            post_comment = Comment.objects.create(
                user=self.request.user, description=comment)
            post_comment.post = blog_post
            print(post_comment.description)
            print(post_comment.user.username)
            print(post_comment.pk)

            resp["description"] = post_comment.description
            resp["pk"] = post_comment.get_absolute_url()
            resp["post_date"] = post_comment.post_date
            resp["get_username"] = post_comment.user.username
            post_comment.save()
            print(resp)
            return JsonResponse(resp, content_type="application/json")

            print("Got Here")
        return JsonResponse(resp, content_type="application/json")
        return HttpResponseRedirect(reverse('blog:blog-detail', args=[pk]))
        # else:
        #     return render(request, 'blog/blog_detail.html', {
        #         "blog_post": blog_post,
        #         "comment_form": comment_form

        #     })


# class BlogTemplateView(View):
#     template_name = "blog/blog_detail.html"

#     def get_context_data(self, **kwargs):
#         context = super(BlogTemplateView, self).get_context_data(**kwargs)
#         blog_posts = BlogPost.objects.all()

#         context.update(list(blog_posts))

#         context["blog_post"] = get_object_or_404(
#             BlogPost, pk=self.kwargs["pk"])
#         print(context["blog_posts"])
#         print("Here")
#         print(context["blog_post"])
#         return context


class BlogListView(ListView):
    template_name = 'blog/blog_list.html'
    model = BlogPost
    paginate_by = 5
    ordering = ['-post_date']
    context_object_name = 'blog_list'

    def get_queryset(self):
        return super(BlogListView, self).get_queryset()
        # return BlogPost.available_posts.all()


class BloggersListView(ListView):
    template_name = 'blog/bloggers_list.html'
    model = Bloggers
    context_object_name = 'bloggers_list'


# class BloggerDetailView(DetailView):
#     template_name = 'blog/blogger_detail.html'
#     model = Bloggers
#     context_object_name = 'single_blogger'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         single_blogger = get_object_or_404(Bloggers, pk=self.kwargs['pk'])
#         user_profile = get_object_or_404(Profile, user=self.request.user)
#         user_form = UserUpdateForm(instance=self.request.user)
#         profile_form = ProfileForm(instance=user_profile)

#         if self.request.method == "POST":
#             profile_form = ProfileForm(
#                 self.request.POST, self.request.FILES, instance=user_profile)
#             user_form = UserUpdateForm(
#                 self.request.POST, instance=self.request.user)

#             if profile_form.is_valid() and user_form.is_valid():
#                 main_user = user_form.save()
#                 main_profile = profile_form.save(False)
#                 main_user.user = main_profile
#                 main_user.save()

#                 return HttpResponseRedirect(reverse('blogger', args=[self.kwargs["pk"]]))
#         else:

#             context["single_blogger"] = single_blogger
#             context["user_form"] = user_form
#             context["profile_form"] = profile_form
#             context["user_profile"] = user_profile
#             return context
class BloggerDetailView(LoginRequiredMixin, View):

    # def post(self, request, pk, *args, **kwargs):
    #     single_blogger = User.objects.get(pk=pk)
    #     user_profile = get_object_or_404(Profile, user=single_blogger)

    #     user_form = UserUpdateForm(
    #         request.POST, instance=request.user)
    #     profile_form = ProfileForm(
    #         request.POST, request.FILES, instance=user_profile)

    #     if profile_form.is_valid() and user_form.is_valid():
    #         user_form.save()
    #         profile_form.save()

    #         return redirect(reverse('blogger', args=[pk]))

    # else:
    #     return render(request, "blog/blogger_detail.html",
    #                   {
    #                       "user_form": user_form,
    #                       "profile_form": profile_form
    #                   })

    def get(self, request, pk):
        single_blogger = User.objects.get(pk=pk)
        user_profile = get_object_or_404(Profile, user=single_blogger)
        profile_form = ProfileForm(instance=user_profile)
        user_form = UserUpdateForm(instance=request.user)

        context = {}
        context["single_blogger"] = single_blogger
        context["user_form"] = user_form
        context["profile_form"] = profile_form
        context["user_profile"] = user_profile

        return render(request, "blog/blogger_detail.html", context)


def home(request):
    blog_posts = BlogPost.available_posts.all()
    blog_posts_count = blog_posts.count()

    return render(request, 'blog/index.html', {
        "blog_posts": blog_posts,
        "blog_posts_count": blog_posts_count
    })


def index(request):
    blog_posts = BlogPost.available_posts.all()

    blog_posts_count = blog_posts.count()
    all_bloggers = Bloggers.objects.all().count()

    return render(request, 'index.html', {
        "blog_posts": blog_posts,
        "blog_posts_count": blog_posts_count,
        "all_bloggers": all_bloggers,
    })


class ChangePasswordView(PasswordChangeView):
    template_name = "blog/change_password.html"
    success_url = reverse_lazy('')


def edit_profile(request, pk):
    single_blogger = User.objects.get(pk=pk)
    user_profile = get_object_or_404(Profile, user=single_blogger)
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=user_profile)
        print("Here")

        if user_form.is_valid() and profile_form.is_valid():
            print("here 3")
            main_user = user_form.save()
            main_profile = profile_form.save(False)
            main_user.user = main_profile
            main_user.save()
            print('Here')
        return HttpResponseRedirect(reverse('blog:blogger', args=[pk]))
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(
            instance=user_profile)
        context = {}
        context["single_blogger"] = single_blogger
        context["user_form"] = user_form
        context["profile_form"] = profile_form
        context["user_profile"] = user_profile

        return render(request, "blog/edit_profile.html", context)


def create_post(request):
    author = request.user

    if request.method == "POST":
        post_create_form = BlogPostCreateForm(request.POST)
        if post_create_form.is_valid():
            title = post_create_form.cleaned_data.get("title")
            description = post_create_form.cleaned_data.get("description")

        new_post = BlogPost.objects.create(
            title=title, description=description, author=author)
        new_post.save()

        return redirect('blog-list')

    else:
        post_create_form = BlogPostCreateForm()

        context = {
            "post_form": post_create_form
        }
    return render(request, "blog/create_post.html", context)


def edit_post(request, pk):
    if request.method == "POST":
        blog_post = get_object_or_404(BlogPost, pk=pk)

        post_create_form = BlogPostCreateForm(request.POST, instance=blog_post)
        if post_create_form.is_valid():
            post_create_form.save()

            return redirect(reverse('blog:blog-detail', args=[pk]))
    else:
        blog_post = get_object_or_404(BlogPost, pk=pk)
        post_create_form = BlogPostCreateForm(request.GET)
        context = {
            "post_form": post_create_form,
            "blog_post": blog_post
        }
        return render(request, "blog/edit_post.html", context)


@login_required
def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.is_deleted = True
    post.save()

    # post.save()
    return redirect(reverse('blog:blog-detail', args=[pk]))


@login_required
def un_delete_post(request, pk):

    post = get_object_or_404(BlogPost, pk=pk)
    post.is_deleted = False
    post.save()
    return redirect(reverse('blog:blog-detail', args=[pk]))


@login_required
def delete_comment(request, pk, comment_pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comment = Comment.objects.get(post__pk=pk, pk=comment_pk)
    if request.user.id == post.author.user.id:
        comment.is_deleted = not comment.is_deleted
        comment.save()

    return redirect(reverse('blog:blog-detail', args=[pk]))


@login_required
def save_comment(request, post_pk):
    blog_post = BlogPost.objects.get(pk=post_pk)

    if request.method == "POST":
        comment = request.POST.get('comment', None)
        data = request.POST.get("success")
        error = request.POST.get("error")

        print('Got Here')

        post_comment = Comment.objects.create(description=comment)
        post_comment.user = request.user,
        post_comment.post = blog_post
        post_comment.save()
        return JsonResponse(data['success'], safe=False)

    else:
        return JsonResponse(error["error"], safe=False)


def like_post_view(request, pk):

    if request.method == "POST":
        user = request.user
        post_id = request.POST.get("post_id")
        liked = False
        blog_post = get_object_or_404(BlogPost, pk=post_id)
        print("------", "now", blog_post)

        total_likes = blog_post.total_likes() or blog_post.likes.all().count()
        if blog_post.likes.filter(id=request.user.id).exists() or user in blog_post.likes.all():
            blog_post.likes.remove(request.user)
            liked = False
        else:
            blog_post.likes.add(request.user)
            liked = True
        users_that_liked_post = blog_post.likes.all()
        resp = {
            "total_likes": total_likes,
            "liked": liked
        }
        print(resp)
        return JsonResponse(resp, content_type="application/json")
    else:
        return HttpResponseRedirect(reverse('blog:blog-detail', args=[pk]))


@login_required
def SearchView(request):
    if request.method == 'POST':
        kerko = request.POST.get('search')
        print(kerko)
        results = User.objects.filter(username__contains=kerko)
        context = {
            'results': results
        }
        return render(request, 'users/search_result.html', context)
