from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation

from utils.models import DateTimeBase

# Create your models here.

class Comment(DateTimeBase):
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=300)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return u"%s" % self.comment


class  Article(DateTimeBase):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User)
    comments = GenericRelation(Comment)

    def __unicode__(self):
        return u"%s" % self.title



