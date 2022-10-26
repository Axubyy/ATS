
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


# router.register('stream', views.StreamPlatformR,
#                 basename='streamplatform')
urlpatterns = [
    path('login/', views.CustomAuthToken.as_view(), name='login'),
    path('register/', views.reqistration_view, name='register'),
    path('list/', views.QuestionListAV.as_view(), name="question-list"),
    path('list/<int:pk>/',
         views.QuestionListDetailAV.as_view(), name="question-detail"),
    path('list/<int:pk>/choices/',
         views.ChoiceListAV.as_view(), name="choice-list"),
    path('list/<int:pk>/choices/<int:choice_pk>/',
         views.ChoiceListDetailAV.as_view(), name="choice-detail"),
]
