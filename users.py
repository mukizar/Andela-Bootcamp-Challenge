"""Handling signin and signup instances of the application"""
user = {'a': 'bcd'} # pylint: disable=invalid-name

class UsersHandler(object):
    """class with methods to handle signin and signup for users"""

    def __init__(self, email, password, name=None):
        self.name = name
        self.email = email
        self.password = password

    def signup(self):
        """function handles signup """
        if self.email and self.password:
            if self.email in user:
                return 'Email already used'
            else:
                if self.password != None:
                    user[self.email] = [self.name, self.password]
                    return user
                else:
                    return 'Input password'
        else:
            return 'user name not entered'

    def sign_in(self):
        """fuction that handles signin"""
        if self.email in user:
            if self.password == user[self.email][1]:
                return 'signed in'
            else:
                return 'Incorrect password'
        else:
            return 'Unknown user'
