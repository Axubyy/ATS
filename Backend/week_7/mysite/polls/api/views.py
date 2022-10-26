
from random import choice
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.generics import (GenericAPIView,
                                     ListCreateAPIView,
                                     ListAPIView,
                                     CreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import ChoiceListSerializer, QuestionSerializer, RegistrationSerializer
from polls.models import Choice, Question
from django.contrib.auth.models import User


@api_view(['POST', 'GET'])
def reqistration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            data = {}
            username = serializer.validated_data.get("username")
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")
            # password2 = serializer.validated_data.get("password2")
            account = User.objects.create(username=username, email=email)
            account.set_password(password)
            account.save()

            data["response"] = "Registration successful!"
            data["first_name"] = account.first_name
            data["last_name"] = account.last_name
            data["username"] = account.username
            data["email"] = account.email

            token, created = Token.objects.get_or_create(user=account)
            data["token"] = token.key

            return Response(data)
            # return Response(serializer.data)
        data = serializer.errors
        return Response(data)
    return Response()


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        account = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=account)
        return Response({
            'token': token.key,
            'username': account.username,
            'email': account.email
        })


class QuestionListAV(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionListDetailAV(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceListAV(ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceListSerializer

    def get_queryset(self):
        return self.queryset.filter(question=self.kwargs.get('pk', None))

    def perform_create(self, serializer):
        question = get_object_or_404(Question, pk=self.kwargs.get('pk', None))
        serializer.save(question=question)


class ChoiceListDetailAV(RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceListSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        choice = Choice.objects.get(question=pk,
                                    pk=self.kwargs.get('choice_pk', None))
        serializers = ChoiceListSerializer(
            choice, context={'request': request})
        return Response(serializers.data)
