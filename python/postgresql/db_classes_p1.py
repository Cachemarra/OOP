"""
Creation of classes to manage postgresql connections

Classes:

    Connection:
        Parameters:
            DATABASE: str <<static>>
            USERNAME: str <<static>>
            PASSWORD: str <<static>>
            DB_PORT: int <<static>>
            HOST: str <<static>>
            connection: Connection <<static>>
            cursor: Cursor <<static>>

        Methods:
            getConnection(cls): Connection <<Class Method>>
            getCursor(cls): Cursor <<Class Method>>
            closeConnection(cls): None <<Class Method>>

        Responsabilities:
            Manage the connection to the database

    Person:
        Parameters:
            personid: int <<Instance Attribute>>
            firstname: str <<Instance Attribute>>
            lastname: str <<Instance Attribute>>
            mail: str <<Instance Attribute>>

        Methods:
            __str__(self): str <<Instance Method>>
            Getters and Setters
        
        Responsabilities:
            Create Person entities objects.
        
    PersonDAO: (Data Access Object)
        Parameters:
            SELECTION: str <<static>>
            INSERTION: str <<static>>
            UPDATE: str <<static>>
            DELETION: str <<static>>
        
        Methods:
            select(cls, personid): Person <<Class Method>>
            insert(cls, person): None <<Class Method>>
            update(cls, person): None <<Class Method>>
            delete(cls, person): None <<Class Method>>
        
        Responsabilities:
            Manage operations over the database of person entities.

"""

#%% Creation of classes and import of libraries
import psycopg2
import logging as log
import sys # To exit the program

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('data_layer.log'),
                    log.StreamHandler()
                ])


class Person:
    
    def __init__(self, personid: int=None, firstname: str = None, lastname: str = None, mail: str = None):
        self._personid = personid
        self._firstname = firstname
        self._lastname = lastname
        self._mail = mail

    def __str__(self):
        return f"PersonID: {self.personid}, FullName: {self.firstname} {self.lastname}, email: {self.mail}"

    # Getters and Setters
    @property
    def personid(self):
        return self.__personid

    @property
    def firstname(self):
        return self.__firstname
    
    @property
    def lastname(self):
        return self.__lastname

    @property
    def mail(self):
        return self.__mail

    @personid.setter
    def personid(self, value):
        self.__personid = value

    @firstname.setter
    def firstname(self, value):
        self.__firstname = value
    
    @lastname.setter
    def lastname(self, value):
        self.__lastname = value

    @mail.setter
    def mail(self, value):
        self.__mail = value



class Connection:

    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'root'
    _DB_PORT = 5432
    _HOST = 'localhost'
    _connection = None
    _cursor = None

    @classmethod
    def getConnection(cls):
        # If there's no connection, create one
        if cls._connection is None:
            try:
                cls._connection = psycopg2.connect(
                    database=cls._DATABASE,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    host=cls._HOST
                )
                
                log.debug(f'[SUCCESS] Connected to Database {cls._connection}')
                
                return cls._connection
            except Exception as e:
                log.error(f"Error connecting to the database: {e}")
                sys.exit(1)

        else:
            return cls._connection
    

    @classmethod
    def getCursor(cls):
        # If there's no cursor, create one
        if cls._cursor is None:
            try:
                cls._cursor = cls.getConnection().cursor()
                log.debug(f'[SUCCESS] Cursor created {cls._cursor}')
                return cls._cursor

            except Exception as e:
                log.error(f"Error creating cursor: {e}")
                sys.exit(1)

        return cls.cursor

    
    @classmethod
    def closeConnection(cls):
        # Close the connection
        if cls.connection is not None:
            cls.cursor.close()
            cls.connection.close()
            cls.connection = None
            cls.cursor = None


class PersonDAO:
    # Class attributes
    SELECTION = "SELECT * FROM person WHERE personid = %s"
    INSERTION = "INSERT INTO person (first_name, last_name, email) VALUES(%s, %s, %s)"
    UPDATE = "UPDATE person SET first_name = %s, last_name = %s, email = %s WHERE personid = %s"
    DELETION = "DELETE FROM person WHERE personid = %s"

    # class methods
    @classmethod
    def select(cls, personid) -> Person:
        # Create a connection
        connection = Connection.getConnection()
        # Create a cursor
        cursor = Connection.getCursor()
        # Execute the query
        cursor.execute(cls.SELECTION, (personid,))
        # Get the result
        result = cursor.fetchone()
        # Close the connection
        Connection.closeConnection()
        # Create the object
        return Person(result[0], result[1], result[2], result[3])




#%% Test
if __name__ == "__main__":
    
    # Testing person class
    person = Person(1, "John", "Doe", "jdoe@mail.com")
    
    log.debug(person)

    # Create a connection
    # Testing Connection class
    Connection.getConnection()

    # Testing Cursor 
    Connection.getCursor()



# %%
