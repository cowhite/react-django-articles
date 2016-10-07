from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
from django.test import Client
from .models import *
from django.contrib.auth.models import User
from .views import *
import json


class ArticleTests(APITestCase):
    #urls = 'articles.urls'

    def setUp(self):
        self.user1 = User.objects.create(username='testuser')
        self.user1.set_password('a')
        self.user1.save()

    def test_create_article_after_login(self):

        ''' Logged in '''

        cl = Client()
        cl.login(username="testuser", password="a")

        ''' Post Article Details after Login '''

        # url_articles = "/api/articles/"
        url_articles = reverse("articles")
        data_new = {
            "title": 'abcd',
            "content": 'Hi'
        }

        res_new_article = cl.post(url_articles, data = data_new, format='json')
        self.assertEqual(res_new_article.status_code, 201)
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(res_new_article.data['title'], data_new['title'])

        ''' Modify Article Details '''
        article_id = res_new_article.data['id']
        url_article = "/api/articles/" + str(article_id)

        modified_data = {
            "content" : 'Hello'
        }

        res_modified_article = cl.put(url_articles, data = modified_data, format='json')
        self.assertEqual(res_modified_article.status_code, 201)
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(res_modified_article.data['title'], modified_data['title'])


        '''Logged out '''

        cl.logout()


    def test_create_article_without_login(self):

        cl = Client()
        ''' Post Article Details without Login '''
        url_articles = "/api/articles/"
        data = {
            "title": 'abcd',
            "content": 'Hi, How are you?'
        }

        res = cl.post(url_articles, data = data, format='json')
        self.assertEqual(res.status_code, 403)
        self.assertEqual(Article.objects.count(), 0)
        self.assertEqual(res.data['detail'], "Authentication credentials were not provided.")


class ArticleCommentTests(APITestCase):
    urls = 'articles.urls'

    def setUp(self):
        self.user1 = User.objects.create(username='testuser')
        self.user1.set_password('a')
        self.user1.save()

    def test_comment_article_after_login(self):

        ''' Logged in '''

        cl = Client()
        cl.login(username="testuser", password="a")

        ''' Create Article Details after Login '''

        url_articles = "/api/articles/"
        data_article = {
            "title": 'abcd',
            "content": 'Hi, How are you?'
        }

        res_article = cl.post(url_articles, data = data_article, format='json')
        self.assertEqual(res_article.status_code, 201)
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(res_article.data['title'], data_article['title'])

        ''' Post Comment for Article '''

        article_id = res_article.data['id']
        url_comment = "/api/articles/"+ str(article_id) +"/comments/"
        data_comment = {
            "comment" : "Looks good"
        }

        res_comment = cl.post(url_comment, data = data_comment, format='json')
        self.assertEqual(res_comment.status_code, 201)
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(res_comment.data['comment'], data_comment['comment'])

        '''Logged out '''

        cl.logout()




