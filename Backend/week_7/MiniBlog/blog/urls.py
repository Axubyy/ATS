import imp
from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = "home"

urlpatterns = [

    path('', views.home, name="home"),
    path('blog/', views.BlogListView.as_view(), name="blog_list"),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name="blog_detail")

]
