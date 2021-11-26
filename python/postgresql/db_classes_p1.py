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
    
    def __init__(self, personid: str=None, firstname: str = None, lastname: str = None, mail: str = None):
        self._personid = personid
        self._firstname = firstname
        self._lastname = lastname
        self._mail = mail

    def __str__(self):
        return f"PersonID: {self._personid}, FullName: {self._firstname} {self._lastname}, email: {self._mail}"

    # Getters and Setters
    @property
    def personid(self):
        return self._personid

    @property
    def firstname(self):
        return self._firstname
    
    @property
    def lastname(self):
        return self._lastname

    @property
    def mail(self):
        return self._mail

    @personid.setter
    def personid(self, value):
        self._personid = value

    @firstname.setter
    def firstname(self, value):
        self._firstname = value
    
    @lastname.setter
    def lastname(self, value):
        self._lastname = value

    @mail.setter
    def mail(self, value):
        self._mail = value



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

        return cls._cursor

    
    @classmethod
    def closeConnection(cls):
        # Close the connection
        if cls._connection is not None:
            cls._cursor.close()
            cls._connection.close()
            cls._connection = None
            cls._cursor = None


class PersonDAO:
    '''
    DAO: Data Access Object
    CRUD: Create, Read, Update, Delete
    '''
    # Class attributes
    _SELECTION = "SELECT * FROM person ORDER BY  personid"
    _INSERTION = "INSERT INTO person (first_name, last_name, email) VALUES(%s, %s, %s)"
    _UPDATE = "UPDATE person SET first_name = %s, last_name = %s, email = %s WHERE personid = %s"
    _DELETION = "DELETE FROM person WHERE personid = %s"

    # class methods
    @classmethod
    def select(cls) -> Person:
        with Connection.getConnection():
            with Connection.getCursor() as cursor:
                # Execute the query
                cursor.execute(cls._SELECTION)
                # Fetch the results
                result = cursor.fetchall()
                persons = []

                for row in result:
                    person = Person(row[0], row[1], row[2], row[3])
                    persons.append(person)

                log.debug(f'[SUCCESS] Result: {result}')
                return persons


    @classmethod
    def insert(cls, person: Person):

        with Connection.getConnection() as connection:
            with connection.cursor() as cursor:
                values = (person.firstname, person.lastname, person.mail)
                cursor.execute(cls._INSERTION, values)
                log.debug(f'[SUCCESS] Person inserted, {person}')
                return cursor.rowcount


    @classmethod
    def update(cls, person: Person):
        with Connection.getConnection() as connection:
            with connection.cursor() as cursor:
                values = (person.firstname, person.lastname, person.mail, person.personid)  # personid is the primary key
                cursor.execute(cls._UPDATE, values)
                log.debug(f'[SUCCESS] Person updated, {person}')
                return cursor.rowcount


    @classmethod
    def delete(cls, person: Person):
        with Connection.getConnection() as connection:
            with connection.cursor() as cursor:
                values = (person.personid, )
                cursor.execute(cls._DELETION, values)
                log.debug(f'[SUCCESS] Person deleted, {person}')
                return cursor.rowcount




#%% Test
if __name__ == "__main__":
    
    # Testing person class
    person = Person(1, "Benito", "vecinos", "bvecinos@mail.com")
    
    log.debug(person)
    
    # Create a connection
    # Testing Connection class
    Connection.getConnection()

    # Testing Cursor 
    Connection.getCursor()

    # Testing PersonDAO
    inserted_persons = PersonDAO.insert(person)
    log.debug(f'[SUCCESS] {inserted_persons} person inserted')

    # Select objects
    persons = PersonDAO.select()
    for person in persons:
        log.debug(person)
    

    '''    # Update object
    # Modifying the first register
    person1 = Person(1, "Antonio", "Badia", 'produccionessincontexto@mail.com')
    updated_persons = PersonDAO.update(person1)
    log.debug(f'[SUCCESS] {updated_persons} person updated')
    '''

    # Delete object
    personD = Person(personid='16')
    deleted_persons = PersonDAO.delete(personD)
    log.debug(f'[SUCCESS] {deleted_persons} person deleted')

# %%
