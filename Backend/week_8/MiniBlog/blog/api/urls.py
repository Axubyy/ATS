import imp
from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = "blog"

urlpatterns = [
    path("login/", views.LoginAV.as_view(), name="login"),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path("logout/", views.LogoutAV.as_view(), name="login"),

    path('create-post/', views.CreatePostAV.as_view(), name="create-post"),
    path('<int:pk>/delete/', views.DeletePostAV.as_view(), name="delete-post"),
    path('<int:pk>/un-delete/', views.UnDeletePostAV.as_view(),
         name="un-delete-post"),
    path('<int:pk>/edit-post/', views.EditPostAV.as_view(), name="edit-post"),
    path('edit-profile/<int:pk>/',
         views.EditProfileAV.as_view(), name="edit-profile"),

    path('blog/', views.BlogListAV.as_view(), name="blog-list"),
    path('blog/<int:pk>/', views.BlogDetailAV.as_view(), name="blog-detail"),
    path('blog/<int:pk>/<int:comment_pk>/',
         views.DeleteCommentAV.as_view(), name="delete-comment"),
    path('blog/bloggers/', views.BloggersListAV.as_view(), name="bloggers"),
    path('blog/blogger/<int:pk>/',
         views.BloggerDetailAV.as_view(), name='blogger'),
    path('change-password/<int:pk>/', views.ChangePasswordAV.as_view(),
         name="change-password"),

    path('like/<int:pk>/', views.LikePostAV.as_view(), name="like-post"),
    path('save-comment/<int:post_pk>/',
         views.SaveCommentAV.as_view(), name="save-comment")
]
