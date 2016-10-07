from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .models import *
from .serializers import *

class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Article.objects.all()


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    #permission_classes = (IsAuthenticated,)

    def get_object(self):
        return get_object_or_404(Article, id=self.kwargs.get('pk'))


class ArticleCommentsView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        article_obj = get_object_or_404(Article, id=self.kwargs.get('article_pk'))
        return article_obj.comments.all()


    def perform_create(self, serializer):
        article_obj = get_object_or_404(Article, id=self.kwargs.get('article_pk'))
        serializer.save(content_object=article_obj, user=self.request.user )


class ArticleCommentView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        article_obj = get_object_or_404(Article, id=self.kwargs.get('article_pk'))
        return article_obj.comments.get(id=self.kwargs.get('comment_pk'))


# # class CommentTOCommentView(generics.ListCreateAPIView):
# #     serializer_class = CommentSerializer
# #     permission_classes = (IsAuthenticated,)

# #     def get_queryset(self):
# #         #import ipdb;ipdb.set_trace()
# #         article_obj = get_object_or_404(Article, id=self.kwargs.get('article_pk'))
# #         return article_obj.comments.all()


# #     def perform_create(self, serializer):
# #         article_obj = get_object_or_404(Article, id=self.kwargs.get('article_pk'))
# #         comment_obj = article_obj.comments.get(id=self.kwargs.get('comment_pk'))
# #         serializer.save(content_object=comment_obj, user=self.request.user )


# # class CommentTOCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
# #     serializer_class = CommentSerializer
# #     permission_classes = (IsAuthenticated,)

# #     def get_object(self):
# #         article_obj = get_object_or_404(Comment, id=self.kwargs.get('comment_pk'))
#         return article_obj.comments.get(id=self.kwargs.get('comment_pk'))



