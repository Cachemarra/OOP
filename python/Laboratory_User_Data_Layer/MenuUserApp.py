#%% A User menu to test/use the whole project.
from logger_base import log
from userDAO import userDAO
from User import User
import sys

# enumerate

SHOW_USERS = 1
ADD_USER = 2
MODIFY_USER = 3
DELETE_USER = 4
LOG_OFF = 5

#%% Menu

option = 0

print('Welcome!'.center(45, '*'))

# User input
while option != LOG_OFF:
    print('\n')
    print('Show your option.')
    print('1.\t Show users')
    print('2.\t Add User')
    print('3.\t Modify user')
    print('4.\t Delete User')
    print('5.\t Close program.')

    option = int(input('Selection: '))

    if option == SHOW_USERS:
        # Show users option
        users = userDAO.select()
        for user in users:
            log.info(user)

    elif option == ADD_USER:
        print('Adding a new user!')
        username = input("What's the username? ")
        password = input("What's the pasword? ")
        user = User(user_id = '1', username=username, password=password)

        userDAO.insert(user)
        log.info(f'[INFO] User inserted. {user}')

    elif option == MODIFY_USER:
        userid = input("What's the user id to modify? ")
        username = input("What's the new name? ")
        password = input("What's the new password? ")

        user = User(user_id=userid, username=username, password=password)
        updated_user = userDAO.update(user)

        log.info(f'[INFO] User updated. {updated_user}')

    elif option == DELETE_USER:
        userid = input("What's the user id to delete? ")

        deleted_user = userDAO.delete(userid)

        log.info(f'[INFO] User deleted. {deleted_user}')

    elif option == LOG_OFF:
        print('Exiting.')
        sys.exit()

    else:
        print('No valid input. Try again.')
