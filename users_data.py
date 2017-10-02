""" module for users """

registered_users = {"email": ["name", "username", "password"]} # pylint: disable=invalid-name


class Users(object):
    """create class users"""
    def __init__(self, name, username, email, password,):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def signup(self):
        """sign up method"""
        if self.email and self.password:
            if self.email in registered_users:
                return 'User already exists'
            else:
                if self.password != None:
                    registered_users[self.email] = [self.name, self.username, self.password]
                    return registered_users
                else:
                    return 'Input password'
        else:
            return 'No user name given'

    def signin(self):
        """signin method"""
        if self.email in registered_users:
            if self.password == registered_users[self.email][1]:
                return 'Logged in'
            else:
                return 'Incorrect password'
        else:
            return 'You are not register! Please sign up'
