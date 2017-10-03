""" Create tests to check functionality and existence of pages"""

import unittest
from app import app


class FlaskTestCase(unittest.TestCase):
    """Defining the tests"""

    def test_signin(self):
        """function defining the test for the the rendering of the signin page """
        tester = app.test_client(self)
        response = tester.get('/signin', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        """function defining the test for the rendering of the signup page """
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_recipes(self):
        """function defining the test for the rendering of the recipes page"""
        tester = app.test_client(self)
        response = tester.get('/recipes', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_dashboard(self):
        """function defining the test for the  rendering dashboard page """
        tester = app.test_client(self)
        response = tester.get('/dashboard', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_create_recipe(self):
        """function defining the test for the  rendering create recipe page """
        tester = app.test_client(self)
        response = tester.get('/create_recipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_delete_recipe(self):
        """function defining the test for the  rendering dashboard page """
        tester = app.test_client(self)
        response = tester.get('/delete_recipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
