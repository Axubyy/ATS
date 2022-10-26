
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (GenericAPIView,
                                     ListCreateAPIView,
                                     ListAPIView,
                                     CreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     RetrieveUpdateAPIView)
from .serializers import QuestionSerializer
from question.models import Question


class QuestionListAV(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionListDetailAV(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_url_kwargs = 'pk'

    def get(self, request, pk=None, *args, **kwargs):
        question = Question.objects.get(pk=pk)
        serializers = QuestionSerializer(question)

        return Response(serializers.data)

    def post(self, request, pk=None, *args, **kwargs):
        question = Question.objects.get(pk=pk)
        serializers = QuestionSerializer(
            question, data=request.data, context={'request': request})
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
