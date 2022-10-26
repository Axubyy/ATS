from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework.renderers import BrowsableAPIRenderer

from .renderers import CustomRenderer


from .permissions import IsAuthorOrReadOnly, IsProfileOwnerOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .serializers import (BlogPostEditSerializer, BlogPostSerializer, BlogPostCreateSerializer,
                          BloggerSerializer, BlogPostDetailSerializer,
                          BloggerDetailSerializer, RegisterationSerializer,
                          DeleteCommentSerializer,
                          CommentSerializer, BlogPostLikeSerializer,
                          ChangePasswordSerializer, EditProfileSerializer,
                          BlogPostDeleteSerializer, LoginSerializer)
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from ..models import BlogPost, Bloggers, Comment, Profile


class BlogListAV(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


class CreatePostAV(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostCreateSerializer
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


class DeletePostAV(generics.UpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDeleteSerializer
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


class UnDeletePostAV(generics.UpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDeleteSerializer
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


class BlogDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDetailSerializer
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


class EditPostAV(generics.RetrieveUpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostEditSerializer
    permission_classes = [IsAuthorOrReadOnly]
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


class DeleteCommentAV(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.select_related("post")
    serializer_class = DeleteCommentSerializer
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]

    def retrieve(self, request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs.get(
            "comment_pk"), post__pk=kwargs.get("pk"))
        serializer = self.serializer_class(comment)
        return Response(serializer.data)


class BloggersListAV(generics.ListAPIView):
    queryset = Bloggers.objects.all()
    serializer_class = BloggerSerializer
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


class BloggerDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bloggers.objects.all()
    serializer_class = BloggerDetailSerializer
    permission_classes = [IsProfileOwnerOrReadOnly]
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


class LikePostAV(generics.UpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostLikeSerializer
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]

    # def put(self, request, pk=None, *args, **kwargs):
    #     post = get_object_or_404(BlogPost, pk=pk)
    #     serializer = self.serializer_class(
    #         post, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({"message": ""}, status=status.HTTP_200_OK)


class SaveCommentAV(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]

    def perform_create(self, serializer):
        post = get_object_or_404(BlogPost, pk=self.kwargs.get('post_pk'))
        user = self.request.user
        serializer.save(post=post, user=user,
                        description=serializer.validated_data.get("description"))


class ChangePasswordAV(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]

    def put(self, request, pk=None, *args, **kwargs):
        serializer = self.serializer_class(
            get_object_or_404(User, pk=pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Successfully updated your password!"}, status=status.HTTP_200_OK)


class EditProfileAV(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = EditProfileSerializer
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]
    # permission_classes = [IsProfileOwnerrReadOnly]


class LoginAV(TokenObtainPairView):
    serializer_class = LoginSerializer
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


class LogoutAV(APIView):
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({"message": "You have successfully logged-out from the Blog API"}, status=status.HTTP_200_OK)


class RegistrationView(generics.CreateAPIView):
    serializer_class = RegisterationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            first_name = serializer.validated_data.get("first_name")
            last_name = serializer.validated_data.get("last_name")
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")
            # confirm_password = serializer.validated_data.get("password2")
            account = User.objects.create(
                first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            data["status"] = "success"
            data["username"] = account.username
            data["email"] = account.email
            refresh_token = RefreshToken.for_user(account)
            data["refresh_token"] = str(refresh_token)
            data["access_token"] = str(refresh_token.access_token)
            return Response(data, status=status.HTTP_201_CREATED)
        data["error"] = serializer.errors
        data["status"] = "success"
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
