#%%  A modification to personDAO class in db_classes_p1.py
import psycopg2
import logging as log
import sys # To exit the program
from pool_cursor import PoolCursor
from db_classes_p1 import Person

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('data_layer.log'),
                    log.StreamHandler()
                ])





class PersonDAO:
    '''
    DAO: Data Access Object
    CRUD: Create, Read, Update, Delete
    As we have the pool_cursor class, we can change this class to optimize
    '''
    # Class attributes
    _SELECTION = "SELECT * FROM person ORDER BY  personid"
    _INSERTION = "INSERT INTO person (first_name, last_name, email) VALUES(%s, %s, %s)"
    _UPDATE = "UPDATE person SET first_name = %s, last_name = %s, email = %s WHERE personid = %s"
    _DELETION = "DELETE FROM person WHERE personid = %s"

    # class methods
    @classmethod
    def select(cls) -> Person:
        with PoolCursor() as cursor:  # This line has changed
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

        with PoolCursor() as cursor:  # This line has changed
            values = (person.firstname, person.lastname, person.mail)
            cursor.execute(cls._INSERTION, values)
            log.debug(f'[SUCCESS] Person inserted, {person}')
            return cursor.rowcount


    @classmethod
    def update(cls, person: Person):

        with PoolCursor() as cursor:  # This line has changed
            values = (person.firstname, person.lastname, person.mail, person.personid)  # personid is the primary key
            cursor.execute(cls._UPDATE, values)
            log.debug(f'[SUCCESS] Person updated, {person}')
            return cursor.rowcount


    @classmethod
    def delete(cls, person: Person):
        # In case just a number is passed
        if not isinstance(person, Person):
            id = person
        else:
            id = person.personid
        with PoolCursor() as cursor:  # This line has changed
            values = (id, )
            cursor.execute(cls._DELETION, values)
            log.debug(f'[SUCCESS] Person deleted, {person}')
            return cursor.rowcount


#%% 
if __name__ == '__main__':
    # Test the class
    PersonDAO.select()

    # Insertion
    person1 = Person(90, 'John', 'B.Good', 'jbgood')

    PersonDAO.insert(person1)
    print('Insertion'.center(50, '-'))
    persons = PersonDAO.select()
    for person in persons:
        log.debug(person)

    # Update	
    person1 = Person(25, 'John', 'B.Good', 'jbgood@mail.com')
    PersonDAO.update(person1)
    persons = PersonDAO.select()
    print('Update'.center(50, '-'))
    for person in persons:
        log.debug(person)
    

    # deleting
    PersonDAO.delete(24)
    persons = PersonDAO.select()
    print('Delete'.center(50, '-'))
    for person in persons:
        log.debug(person)