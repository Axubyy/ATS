import imp
from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = "blog"

urlpatterns = [

    path('', views.index, name="index"),
    path('blogs/', views.BlogListView.as_view(), name="blog-list"),
    path('<int:pk>/', views.BlogDetailView.as_view(), name="blog-detail"),
    path('bloggers', views.BloggersListView.as_view(), name="bloggers"),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger'),

]
