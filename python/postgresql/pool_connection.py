# Libraries
import logging as log
import sys # To exit the program
from psycopg2 import pool

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('data_layer.log'),
                    log.StreamHandler()
                ])


#%%
# With pool connections you can simplify the code by using the same connection
# Remember, a connection is linked with just 1 user.



class Connection:

    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'root'
    _DB_PORT = 5432
    _HOST = 'localhost'
    # Not needed anymore
    '''
    _connection = None
    _cursor = None
    '''
    # New Variables.
    # A pool connections need to know how many connections are available.
    _MIN_CONNECTIONS = 1
    _MAX_CONNECTIONS = 5 # Don't have to be too big as db have a limit.
    _pool = None


    # New method to configure the pool
    @classmethod
    def getPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CONNECTIONS,
                    cls._MAX_CONNECTIONS,
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port = cls._DB_PORT,
                    database=cls._DATABASE
                )

                log.debug(f'[SUCCESS] Pool created succesfully. {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'[ERROR] An error is raised while obtaining a pool. {e}')
                sys.exit()

        else:
            return cls._pool


    # This class changed from the original version.
    @classmethod
    def getConnection(cls):
        # Get a connection from the pool
        connection = cls.getPool().getconn()
        log.debug(f'[SUCCESS] Connection obtained succesfully. {connection}')
        return connection
        

    # Free connection
    @classmethod
    def freeConnection(cls, connection):
        cls.getPool().putconn(connection) # Put the connection back in the pool
        log.debug(f'[SUCCESS] Connection returned to pool succesfully. {connection}')

    # Close connection
    @classmethod
    def closeConnection(cls, connection):
        cls.getPool().closeall() # Close all connections

    
if __name__ == '__main__':
    print('This is a module. It is not meant to be run as a main program.')
    # Test if we are getting different connections from the pool.

    connection1 = Connection.getConnection()
    # Freeng the connection
    Connection.freeConnection(connection1)
    # Get another connection
    # Remember, the connection limit is 5
    connection2 = Connection.getConnection()
    connection3 = Connection.getConnection()
    connection4 = Connection.getConnection()
    Connection.freeConnection(connection3)
    connection5 = Connection.getConnection()
    connection6 = Connection.getConnection()
    connection7 = Connection.getConnection()


