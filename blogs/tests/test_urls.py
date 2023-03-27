from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blogs.views import HomeView, ArticleCreateView, blogPost, ArticleDeleteView, ArticleUpdateView, editComment, deleteComment

class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_detail_article_url_resolves(self):
        url = reverse('detail-article',args=['some-value'])
        self.assertEquals(resolve(url).func, blogPost)
    
    def test_create_article_url_resolves(self):
        url = reverse('create-article')
        self.assertEquals(resolve(url).func.view_class, ArticleCreateView)

    def test_update_article_url_resolves(self):
        url = reverse('update-article',args=['some-value'])
        self.assertEquals(resolve(url).func.view_class, ArticleUpdateView)
    
    def test_delete_article_resolves(self):
        url = reverse('delete-article',args=['some-value'])
        self.assertEquals(resolve(url).func.view_class, ArticleDeleteView)
    
    def test_editComment_url_resolves(self):
        url = reverse('edit-comment',args=['some-value'])
        self.assertEquals(resolve(url).func, editComment)

    def test_deleteComment_url_resolves(self):
        url = reverse('delete-comment',args=['some-value'])
        self.assertEquals(resolve(url).func, deleteComment)


     