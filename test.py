""" Create tests to check functionality and existence of pages"""

import unittest
from app import app


class FlaskTestCase(unittest.TestCase):
    """Defining the tests"""

    def test_signin(self):
        """function defining the test for the SignInpage """
        tester = app.test_client(self)
        response = tester.get('/signin', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        """function defining the test for the SignUpage """
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_user_dashboard(self):
        """function defining the test for the Postspage """
        tester = app.test_client(self)
        response = tester.get('/posts', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
