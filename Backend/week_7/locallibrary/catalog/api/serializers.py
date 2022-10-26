from catalog.models import Book, Author, Genre
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"

    def create(self, validated_data):
        genres = validated_data.pop("genre")
        authorww = validated_data.pop("author")

        user = self.context.get("request").user
        author = Author.objects.create(
            first_name=user.first_name, last_name=user.last_name)

        book = Book.objects.create(**validated_data)
        for genre in genres:
            gen = Genre.objects.create(**genre)
            book.genre.add(gen)
        book.author = author
        book.save()

        return book


class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"

        def update(self, instance, validated_data):
            return instance
