import unittest
from app.models import Article


class TestArticle(unittest.TestCase):
    
    def setUp(self):

        self.new_article = Article('BeauHD','Microsoft Edge Overtakes Safari As Worlds Second Most Popular Desktop Browser','Microsoft Edge has overtaken Apples Safari to become the worlds second most popular desktop browser, based on data provided by web analytics service StatCounter. MacRumors reports: According to the data, Microsoft Edge is now used on 10.07 percent of deskto…','https://tech.slashdot.org/story/22/05/03/2145233/microsoft-edge-overtakes-safari-as-worlds-second-most-popular-desktop-browser','https://a.fsdn.com/sd/topics/internet_64.png','2022-05-04T01:30:00Z')

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    
    def test_init(self):
        self.assertEqual(self.new_article.author,'BeauHD')
        self.assertEqual(self.new_article.title,'Microsoft Edge Overtakes Safari As Worlds Second Most Popular Desktop Browser')
        self.assertEqual(self.new_article.description,'Microsoft Edge has overtaken Apples Safari to become the worlds second most popular desktop browser, based on data provided by web analytics service StatCounter. MacRumors reports: According to the data, Microsoft Edge is now used on 10.07 percent of deskto…')
        self.assertEqual(self.new_article.url,'https://tech.slashdot.org/story/22/05/03/2145233/microsoft-edge-overtakes-safari-as-worlds-second-most-popular-desktop-browser')
        self.assertEqual(self.new_article.image,'https://a.fsdn.com/sd/topics/internet_64.png")
        self.assertEqual(self.new_article.publish_date,'22022-05-04T01:30:00Z')