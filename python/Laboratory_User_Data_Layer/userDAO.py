#%% User DAO class.

from logger_base import log
from PoolCursor import PoolCursor
from User import User

#%% DAO class.

class userDAO:
    # DAO -> Data Access Object.
    # CRUD -> Create, Read, Update, Delete.

    # Class/static parameters. 

    _SELECT = 'SELECT * FROM users'
    _INSERT = 'INSERT INTO users(username, password) VALUES(%s, %s)'
    _UPDATE = 'UPDATE users SET username = %s, password = %s WHERE userid = %s'
    _DELETE = 'DELETE FROM users WHERE userid = %s'

    # classmethods

    @classmethod
    def select(cls):
        with PoolCursor() as cursor:
            # Executing the query
            cursor.execute(cls._SELECT)

            # Fetching values
            result = cursor.fetchall()
            users = []

            for row in result:
                user = User(row[0], row[1], row[2])
                users.append(user)

            log.debug(f'[SUCCESS] Data retrieved succesfully.\n {result}')
            return users
        

    @classmethod
    def insert(cls, user: User):
        with PoolCursor() as cursor:
            values = (user.username, user.password)
            cursor.execute(cls._INSERT, values)

            log.debug(f'[SUCCESS] User inserted in the database. {user}')
            return cursor.rowcount

    
    @classmethod
    def update(cls, user: User):
        with PoolCursor() as cursor:
            values = (user.username, user.password, user.userid)
            cursor.execute(cls._UPDATE, values)

            log.debug(f'[SUCCESS] User updated successfully. {user}')
            return cursor.rowcount


    @classmethod
    def delete(cls, user: User):
        # In case a number is passed:
        if not isinstance(user, User):
            userid = str(user)

        else: 
            userid = user.userid

        with PoolCursor() as cursor:
            # Retrieving User data
            values = (userid, )
            cursor.execute(cls._DELETE, values)

            log.debug(f'[SUCCESS] User deleted succesfully. {user}')
            return cursor.rowcount
            

#%% Testing

if __name__ == '__main__':

    # Select method
    users = userDAO.select()
    # printing users
    print('Select'.center(45, '-'))
    for user in users:
        print(user)
    print('\n')

    # Insert method
    print('Insert'.center(45, '-'))
    user = User('10', 'Albert', 'pAzSW0rd')
    userDAO.insert(user)
    print('\n')

    # Update
    print('Update'.center(45, '-'))
    user = User('2', 'Antonio', 'lEYendYT4s')
    userDAO.update(user)
    userDAO.select()
    print('\n')

    # Delete
    print('Delete'.center(45, '-'))
    userDAO.delete(4)
    userDAO.select()

