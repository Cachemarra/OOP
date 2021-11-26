#%% User class

from logger_base import log

#%% Class to add users to the dataset

class User:

    def __init__(self, user_id: str, username: str, password: str):
        self._user_id = user_id
        self._username = username
        self._password = password

    # Methods. 
    # __str__
    def __str__(self) -> str:
        return f'UserID: {self._user_id}, username: {self._username}, password: {self._password}.'
    
    # Getters    
    @property
    def userid(self):
        return self._user_id

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    # Setters
    @userid.setter
    def userid(self, value):
        self._user_id = value
    
    @username.setter
    def username(self, value):
        self._username = value
    
    @password.setter
    def password(self, value):
        self._password = value


#%% Testing the class

if __name__ == '__main__':
    
    user1 = User('1', 'Pedro', 'password123')
    user2 = User('2', 'Johny', 'hard54321')

    # Printing user1 data
    print('User1 Data'.center(45, '-'))
    print(user1)
    print('\n')

    # Printing user2 data
    print('User2 data'.center(45, '-'))
    print(user2)

