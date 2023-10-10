import unittest
from io import StringIO

class TestHitlogAnalysis(unittest.TestCase):
    def test_find_top_articles(self):
        articles_counter = Counter({'/articles/1': 3, '/articles/2': 2, '/articles/3': 1})
        top_articles = find_top_articles(articles_counter, 3)
        expected_top_articles = [('/articles/1', 3), ('/articles/2', 2), ('/articles/3', 1)]
        self.assertEqual(top_articles, expected_top_articles)

    def test_write_to_csv(self):
        top_articles = [('/articles/1', 3), ('/articles/2', 2), ('/articles/3', 1)]
        output_file = StringIO()
        write_to_csv(output_file, top_articles)
        expected_output = "page_name,page_url,total\nArticle,/articles/1,3\nArticle,/articles/2,2\nArticle,/articles/3,1\n"
        self.assertEqual(output_file.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
