from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'comment', 'user_name' )
        read_only_fields = ('content_object', 'user',)

    def get_user_name(self, obj):
        return obj.user.username


class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    # comments = CommentSerializer(allow_null=True, read_only=True)

    class Meta:
        model = Article
        read_only_fields = ('author',)

    def get_author_name(self, obj):
        return obj.author.username


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, required=False)
    password = serializers.CharField(
                    style={'input_type': 'password'}
                )
    email = serializers.EmailField(required=False)
