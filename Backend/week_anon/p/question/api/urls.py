
from django.urls import path, include
from . import views


# router.register('stream', views.StreamPlatformR,
#                 basename='streamplatform')
urlpatterns = [
    path('list/', views.QuestionListAV.as_view(), name="question-list"),
    path('<int:question_pk>/',
         views.QuestionListDetailAV.as_view(), name="question-detail"),
]
