""" Create tests to check functionality of user methods"""

import unittest
from users_data import Users, registered_users


class UserModelTest(unittest.TestCase):
    """Defining the tests"""

    def test_User_Instance(self):
        """this test ensures that the object is always properly initialized"""
        registered_users = Users('rmukiza@gmail.com', 'abc', 'cd')
        self.assertIsInstance(registered_users, Users, msg='object missing parameters')

    def test_signup_user_added_to_user_dictionary(self):
        """test if regisetered user is added to list"""
        registered_users = Users('rmukiza@gmail.com','rayner45', 'Rayner', 'rmukiza')
        self.assertEqual({'email': [], 'rmukiza@gmail.com': ['Rayner', 'rmukiza', 'rayner45']}, registered_users.signup())
  
    def test_wrong_password_on_signin(self):
        registered_users= Users('rmukiza@gmail.com', 'abcd')
        self.assertEqual(registered_users.signin(), 'Incorrect password')

if __name__ == '__main__':
    unittest.main()
