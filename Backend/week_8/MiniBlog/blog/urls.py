import imp
from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = "blog"

urlpatterns = [
    path('create-post/', views.create_post, name="create-post"),
    path('<int:pk>/delete/', views.delete_post, name="delete-post"),
    path('<int:pk>/un-delete/', views.un_delete_post, name="un-delete-post"),
    path('<int:pk>/edit-post/', views.edit_post, name="edit-post"),
    path('edit-profile/<int:pk>/', views.edit_profile, name="edit-profile"),
    path('', views.index, name="index"),
    path('blogs/', views.BlogListView.as_view(), name="blog-list"),
    path('<int:pk>/', views.BlogDetailView.as_view(), name="blog-detail"),
    path('<int:pk>/<int:comment_pk>/',
         views.delete_comment, name="delete-comment"),
    path('bloggers', views.BloggersListView.as_view(), name="bloggers"),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger'),
    path('change-password/', views.ChangePasswordView.as_view(),
         name="change-password"),
    #     path('save-comment/<int:post_pk>', views.save_comment, name="save-comment")



]
