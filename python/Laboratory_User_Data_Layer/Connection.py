#%%  Connection class.

from os import close
from psycopg2 import pool
import logging as log
import sys # To exit the program

# Basic configuration for the logger
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p'
                )


#%%  Connection class.
class Connection:

    # Static/class parameters

    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'root'
    _DB_PORT = 5432
    _HOST = 'localhost'
    _MIN_CONNECTIONS = 1
    _MAX_CONNECTIONS = 5
    _pool = None

    # Methods

    @classmethod
    def getPool(cls):
        '''
        Method to get a pool connection
        '''
        # Check if there's no connection to the pool
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CONNECTIONS,
                    cls._MAX_CONNECTIONS,
                    host = cls._HOST,
                    user = cls._USERNAME,
                    password = cls._PASSWORD,
                    port = cls._DB_PORT,
                    database = cls._DATABASE
                )

                log.debug(f'[SUCCESS] Pool created succesfully. {cls._pool}')
                return cls._pool

            # Is dangerous to keep program open if an error happens, so we close it.
            except Exception as err: 
                log.error(f'[ERROR] An error has occurred obtaining a pool connection. {err}')
                sys.exit()

        else:
            return cls._pool


    @classmethod
    def getConnection(cls):
        '''
        Method to get the connection from a pool.
        '''
        connection = cls.getPool().getconn()
        log.debug(f'[SUCCESS] Connection stablished succesfully. {connection}')
        return connection


    @classmethod
    def freeConnection(cls, connection):
        '''
        Method to free a connection from the pool.
        '''
        cls.getPool().putconn(connection) # Return the connection to the pool.
        log.debug(f'[SUCCESS] Connection returned to the pool succesfully. {connection}')
        pass


    @classmethod
    def closeConnection(cls):
        """
        Method for close the connection with the database.
        """
        cls.getPool().closeall()

        log.debug('[SUCCESS] All Connections closed succesfully.')



#%% Testing
if __name__ == '__main__':

    # Testing getting pool
    # Creatting a connection to the pool
    connection = Connection.getPool()

    # Getting connections
    connection2 = Connection.getConnection()
    connection3 = Connection.getConnection()
    connection4 = Connection.getConnection()

    # Freeing a connection
    Connection.freeConnection(connection2)

    # Closing all connections.
    Connection.closeConnection()




