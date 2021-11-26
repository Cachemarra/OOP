#%% User DAO class.

import psycopg2
import logging as log
import sys # To exit the program
import PoolCursor
import User
from postgresql.db_classes_p1 import Person, PersonDAO


log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p'
                )



#%% DAO class.

class userDAO:
    # DAO -> Data Access Object.
    # CRUD -> Create, Read, Update, Delete.

    # Class/static parameters. 

    _SELECT = 'SELECT * FROM persona'
    _INSERT = 'INSERT INTO person(userid, username, password) VALUES(%s, %s, %s)'
    _UPDATE = 'UPDATE person SET userid = %s, username = %s, password = %s'
    _DELETE = 'DELETE FROM person WHERE userid = %s'

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
            values = (user.userid, user.username, user.password)
            cursor.execute(cls._INSERT, values)

            log.debug(f'[SUCCESS] User inserted in the database. {user}')
            return cursor.rowcount

    
    @classmethod
    def update(cls, user: User):
        with PoolCursor() as cursor:
            values = (user.userid, user.username, user.password)
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
    user = Person('10', 'Albert', 'pAzSW0rd')
    userDAO.insert(user)

    # Update
    print('Update'.center(45, '-'))
    user = Person('1', 'Antonio', 'lEYendYT4s')
    userDAO.update(user)
    userDAO.select()

    # Delete
    print('Delete'.center(45, '-'))
    userDAO.delete(25)
    userDAO.select()

