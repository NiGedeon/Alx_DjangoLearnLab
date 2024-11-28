from rest_framework import serializers
from api.models import Author, Book
from datetime import date

#This Model serializer is used to serialize and deserialize the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self,value):
        current_year = date.today().year

        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future!")
        return value

#This Model serializer is used to serialize and deserialize the Author model
class AuthorSerializer(serializers.ModelSerializer):
    #Nesting the serializers so that they handle a one to many relationship
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ["name","books"]
