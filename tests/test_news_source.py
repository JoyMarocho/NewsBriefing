import unittest
from app.models import Source

class TestSource(unittest.TestCase):
    
    def setUp(self):

        self.new_source = Source('bloomberg','bloomberg','Bloomberg delivers business and markets news, data, analysis, and video to the world, featuring stories from Businessweek and Bloomberg News.','http://www.bloomberg.com','en','us')

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    
    def test_init(self):
        self.assertEqual(self.new_source.id,"bloomberg")
        self.assertEqual(self.new_source.name,"bloomberg")
        self.assertEqual(self.new_source.description,"Bloomberg delivers business and markets news, data, analysis, and video to the world, featuring stories from Businessweek and Bloomberg News.")
        self.assertEqual(self.new_source.url,"http://www.bloomberg.com")
        self.assertEqual(self.new_source.language,"en")
        # self.assertEqual(self.new_source.country,"us")

