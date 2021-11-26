#%% Pool Cursor class

from os import close
from psycopg2 import pool
import logging as log
import sys
from Connection import Connection

# Basic configuration for the logger
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p'
                )


#%% Creation of the class

class PoolCursor:
    '''
    Manage the connections and cursor objects obtained by pool connection.
    '''
    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self):
        # Method when using 'with'
        # Getting the connection an the cursor.
        self._conn = Connection.getConnection()
        self._cursor = self._conn.cursor()

        return self._cursor
        

    def __exit__(self, exception_type, exception_value, traceback):
        # Method called when exiting 'with'
        # A commit or rollback will happened depending if there's an error
        
        # If exception_value exists, will apply a rollback
        if exception_value:
            self._conn.rollback()
            log.error(f'[ERROR] An exception has ocurred, rollbacking. \n Error Message: {value}, {type}, {traceback}')
        
        # No errors nor exceptions
        else:
            # Commiting changes
            self._conn.commit()
            log.debug('[INFO] Transaction commited succesfully.')

        # Closing the cursor
        self._cursor.close()
        Connection.freeConnection(self._conn)
        

#%% Testing PoolCursor class.
if __name__ == '__main__':

    # Remember, using 'with' the class is initialized automatically.

    with PoolCursor() as cursor: # Will enter to __enter__ and it returns a cursor.
        # Creating a query to the database.
        cursor.execute('SELECT * FROM person')
        rows = cursor.fetchall()
        # Checking the data retrieved.
        for row in rows:
            print(row)
    
    sys.exit()