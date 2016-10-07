from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name="articles"),
    url(r'^(?P<pk>[0-9]+)/$', ArticleDetailView.as_view(), name="article"),
    url(r'^(?P<article_pk>[0-9]+)/comments/$', ArticleCommentsView.as_view(), name="comments"),
    url(r'^(?P<article_pk>[0-9]+)/comments/(?P<comment_pk>[0-9]+)/$',
        ArticleCommentView.as_view(), name="comment"),
    # url(r'^(?P<article_pk>[0-9]+)/comments/(?P<comment_pk>[0-9]+)/comments$', CommentTOCommentView.as_view(), name="comments-comment"),
]