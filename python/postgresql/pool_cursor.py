#%% Libraries
import logging as log
import sys # To exit the program
from psycopg2 import pool
from pool_connection import Connection


log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('data_layer.log'),
                    log.StreamHandler()
                ])


#%% Classes

class PoolCursor:
    def __init__(self):
        self._connection = None
        self._cursor = None

    # When using 'with' it calls to __enter__ and __exit__ methods. we are going
    # to override them.

    def __enter__(self):
        log.debug('[INFO] Method __enter__ executed')
        self._connection = Connection.getConnection()
        self._cursor = self._connection.cursor()
        return self._cursor


    # When going out of with
    #               exception_type, exception_value, traceback
    def __exit__(self, type, value, traceback):
        # Commit or rollback of the transaction. If something bad happens, the callback is called.
        log.debug('[INFO] Method __exit__ executed')

        if value: # Exception value happens:
            self._connection.rollback()
            log.error(f'[ERROR] An exception has ocurred, rollback now!.\n Error Message: {value}, {type}, {traceback}')

        else: # There's no exception
            self._connection.commit()
            log.debug('[INFO] Transaction committed succesfully')

        self._cursor.close()
        Connection.freeConnection(self._connection)





#%% Testing
if __name__ == '__main__':
    print('[INFO] This is a module, not a program')

    # This will initialize the PoolCursor class with Nones and enter to __enter__ method
    with PoolCursor() as cursor:

        cursor.execute('SELECT * FROM person')
        rows = cursor.fetchall()
        print(rows)

    sys.exit()