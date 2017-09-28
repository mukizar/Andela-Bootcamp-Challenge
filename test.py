from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    #test if flask was setup correctly
    def test_index(self):
        #use tester to create test
        tester = app.test_client(self)
        response = tester.get('/signin', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    # test if the signin page loads as designed


    def test_signin_page_loads(self):
        
        tester = app.test_client(self)
        response = tester.get('/signin', content_type='html/text')
        self.assertTrue(b'SignIn' in response.data)


if __name__ == '__main__':
    unittest.main()