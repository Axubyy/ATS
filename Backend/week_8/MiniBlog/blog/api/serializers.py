
from django.contrib.auth.password_validation import validate_password
from ..models import Comment, Profile
from blog.models import BlogPost, Bloggers, Tag
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class BloggerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    blogger_url = serializers.SerializerMethodField()

    class Meta:
        model = Bloggers
        fields = "__all__"

    def get_blogger_url(self, obj):
        return self.context.get("request").build_absolute_uri("/api/blog/blogger/") + str(obj.pk) + "/"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class BlogPostCreateSerializer(serializers.ModelSerializer):
    # post_tags = TagSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = BlogPost
        fields = ("title", "description", "tags", )
        # extra_kwargs = {
        #     'tags': {'write_only': True}
        # }

    def create(self, validated_data):
        user = self.context.get('request').user
        blogger = Bloggers.objects.get(pk=user.pk)
        tags = validated_data.pop("tags", None)
        blog = BlogPost.objects.create(**validated_data)
        blog.author = blogger
        for tag in tags:
            print(tag['name'])
            # try:
            #     cre_tag = Tag.objects.get(name=tag["name"])
            # except Tag.DoesNotExist as e:
            #     print(e)
            # if cre_tag:
            #     blog.tags.add(cre_tag)
            # else:
            cre_tag, created = Tag.objects.get_or_create(name=tag["name"])
            blog.tags.add(cre_tag)
        blog.save()

        return blog


class BlogPostSerializer(serializers.ModelSerializer):
    author = BloggerSerializer()
    blog_url = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = "__all__"

    def get_blog_url(self, obj):
        return self.context.get("request").build_absolute_uri("/api/blog/blogger/") + str(obj.pk) + "/"


class BlogPostDetailSerializer(serializers.ModelSerializer):
    author = BloggerSerializer()
    comments = CommentSerializer(many=True)
    tags = TagSerializer(many=True)
    likes = UserSerializer(many=True)
    # comments = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = "__all__"

    def update(self, instance, validated_data):
        user = self.context.get('request').user
        tags = validated_data.pop("tags", None)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description)

        for tag in tags:
            try:
                cre_tag = Tag.objects.get(name=tag.name)
            except Tag.DoesNotExist as e:
                print(e)
            if cre_tag:
                instance.tags.add(cre_tag)
            else:
                cre_tag = Tag.objects.create(name=tag["name"])
                instance.tags.add(cre_tag)
        instance.save()
        return instance

    # def get_comments(self, obj):
    #     return CommentSerializer(obj.comments.all(), many=True).data


class BloggerDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    posts = BlogPostSerializer(many=True, source="author")

    class Meta:
        model = Bloggers
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.bio_info = validated_data.get("bio_info", instance.bio_info)
        instance.user = self.context.get("request").user

        instance.save()
        return instance


class BlogPostEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ("title", "description",)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title")
        instance.description = validated_data.get("description")
        instance.save()
        return instance


class BlogPostDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.is_deleted = not (instance.is_deleted)
        instance.save()
        return instance


class BlogPostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ("likes",)

    def update(self, instance, validate_data):
        print(instance.total_likes())
        user = self.context.get("request").user
        if instance.likes.filter(pk=user.pk).exists():
            instance.likes.remove(user.pk)
        else:
            instance.likes.add(user.pk)
        print(instance.total_likes())
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['liked_by'] = instance.likes.count()

        return representation


class DeleteCommentSerializer(serializers.ModelSerializer):
    post = BlogPostSerializer()

    class Meta:
        model = Comment
        fields = "__all__"


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    new_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ("old_password", "new_password", "confirm_password")

    def validate(self, attrs):

        if attrs.get("new_password") != attrs.get("confirm_password"):
            raise serializers.ValidationError("Passwords don't match!")

        return attrs

    def update(self, instance, validated_data):
        if instance.check_password(validated_data.get("old_password")):
            instance.set_password(validated_data.get("new_password"))
            instance.save()
            return instance
        raise serializers.ValidationError(
            "Incorrect Credentials, Please contact account owner!")


class EditProfileSerializer(serializers.Serializer):
    email = serializers.EmailField(source="user.email")
    first_name = serializers.CharField(source="user.first_name")
    username = serializers.CharField(source="user.username")
    last_name = serializers.CharField(source="user.last_name")
    image = serializers.ImageField(allow_empty_file=True)

    class Meta:
        model = Profile
        fields = ("image", "first_name", "last_name", "email", "username",)

    def update(self, instance, validated_data):
        print(instance.user)
        user = User.objects.get(email=self.context.get("request").user.email)
        user.email = validated_data.get("email", user.email)
        user.first_name = validated_data.get(
            "first_name", user.first_name)
        user.last_name = validated_data.get(
            "last_name", user.last_name)
        user.username = validated_data.get(
            "username", user.username)
        instance.image = validated_data.get("image", instance.image)
        instance.save()
        return instance


class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...
        return token


class RegisterationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', "first_name", "last_name",
                  'email', 'password', 'confirm_password')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def validate_email(self, value):
        lower_email = value.lower()
        if User.objects.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError("Email already in use")
        return lower_email

    # def create(self, validated_data):
    #     account = Account.objects.create_user(
    #         username=validated_data.get('username'), email=validated_data.get('email'), password=validated_data.get('password'), first_name=validated_data.get('first_name'), last_name=validated_data.get('last_name'))

    #     refresh_token = RefreshToken.for_user(account)
    #     account["refresh_token"] = str(refresh_token)
    #     account["access_token"] = str(refresh_token.access_token)
    #     return account
    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        account = super().update(instance, validated_data)
        if password is not None:
            account.set_password(password)
            account.save()
        return account
