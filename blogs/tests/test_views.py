from django.test import TestCase, Client
from django.urls import reverse


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('home')
        # self.detailArticle_url = reverse('detail-article',args=['4'])

    def test_home_view(self):        
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blogs/home.html')

    # def test_detailArticle_view(self):        
    #     response = self.client.get(self.detailArticle_url)

    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response,'blogs/detail-article.html')    

