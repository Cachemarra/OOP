# What's the project?

Create a user data layer with postgreSQL or another SQL engine.

You should be able to create a table and add users, delete or update.

6 classes must be created:

- Connection
- PoolCursor
- User
- UserDAO
- Logger_Base
- Menu (this could not be a class but a main file.)

-----------------------

## Connection
**Parameters:**

    <<static>>
    DATABASE: str
    USERNAME: str
    PASSWORD: str
    DB_PORT: str
    HOST: str
    MIN_CONNECTIONS: int
    MAX_CONNECTIONS: int
    pool: Pool

**Methods:**

    <<classmethods>>
    getPool(cls) -> Pool
    getConnection(cls) -> Connection
    freeConnection(cls, Connection)
    closeConnections(cls)

------------------

## PoolCursor

**Parameters:**

    conn: str
    cursor: str

**Methods:**

    __init__
    __enter__
    __exit__

**Responsabilities:**

Manage the connection and cursor objects obtained over an pool connection.

_enter_ and _exit_ methods are for the `with` implementation to work with cursor.

----------------------

## User

**Parameters:**

    user_id: int
    username: str
    password: str

**Methods:**

    __str__(): str
    Getters
    Setters

**Responsabilities:**

    Create User objects.

----------------------

## UserDAO

**Parameters:**

    <<static>>
    SELECT: str
    INSERT: str
    UPDATE: str
    DELETE: str

**Methods:**

    <<classmethod>>
    select(cls): List<USER>
    insert(cls, User)
    update(cls, User)
    Detele(cls, User)

**Responsabilities:**

    Handle CRUD operations (Create, Read, Update, Delete) over User.

-----------------------

## Logger_base

**Parameters:**

    logger: logging

**Responsabilities:**

    Configure logging for all the app.

----------------------

## MenuUserApp

**Responsabilities:**

Contain a menu with 5 options:

1. List users
2. Add user
3. Update User
4. Delete User
5. Log Off.




