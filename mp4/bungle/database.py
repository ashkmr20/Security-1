import MySQLdb as mdb
from bottle import FormsDict
from hashlib import md5

# connection to database project2
def connect():
    """makes a connection to MySQL database.
    @return a mysqldb connection
    """
    
    #TODO: fill out function parameters. Use the user/password combo for the user you created in 2.1.2.1
    
    return mdb.connect(host="localhost",
                       user="asathis2",
                       passwd="21f84d708af483c2c403575b135002e3260be56d35850e8ab722398cc48ef622",
                       db="");

def createUser(username, password):
    """ creates a row in table named user 
    @param username: username of user
    @param password: password of user
    """

    db_rw = connect()
    cur = db_rw.cursor()
    #TODO: Implement a prepared statement using cur.execute() so that this query creates a row in table user
    cur.execute("USE project2")

    insert_stmt = (
     "INSERT INTO users (username, password) "
    "VALUES (%s, %s)"
    )
    data=  (username,password)
    cur.execute(insert_stmt, data)
    db_rw.commit()

def validateUser(username, password):
    """ validates if username,password pair provided by user is correct or not
    @param username: username of user
    @param password: password of user
    @return True if validation was successful, False otherwise.
    """

    db_rw = connect()
    cur = db_rw.cursor()

    #TODO: Implement a prepared statement using cur.execute() so that this query selects a row from table user
    cur.execute("USE project2")

    select_stmt = (
     "SELECT * from users where username= %s and password = %s "
    )
    cur.execute(select_stmt, (username, password))
    if cur.rowcount < 1:
        return False
    return True

def fetchUser(username):
    """ checks if there exists given username in table users or not
    if user exists return (id, username) pair
    if user does not exist return None
    @param username: the username of a user
    @return The row which has username is equal to provided input
    """

    db_rw = connect()
    cur = db_rw.cursor(mdb.cursors.DictCursor)
    print username
    #TODO: Implement a prepared statement so that this query selects a id and username of the row which has column username = username
    cur.execute("USE project2")

    select_stmt = (
     "SELECT id, username from users where username= %s  "
    )
    cur.execute(select_stmt, username)
    if cur.rowcount < 1:
        return None
    return FormsDict(cur.fetchone())

def addHistory(user_id, query):
    """ adds a query from user with id=user_id into table named history
    @param user_id: integer id of user
    @param query: the query user has given as input
    """

    db_rw = connect()
    cur = db_rw.cursor()
    #TODO: Implement a prepared statment using cur.execute() so that this query inserts a row in table history
    cur.execute("USE project2")
    insert_stmt = (
     "INSERT INTO history (user_id, query) "
    "VALUES (%s, %s)"
    )
    data=  (user_id,query)
    cur.execute(insert_stmt, data)
    db_rw.commit()

#grabs last 15 queries made by user with id=user_id from table named history
def getHistory(user_id):
    """ grabs last 15 distinct queries made by user with id=user_id from 
    table named history
    @param user_id: integer id of user
    @return a first column of a row which MUST be query
    """

    db_rw = connect()
    cur = db_rw.cursor()
    #TODO: Implement a prepared statement using cur.execute() so that this query selects 15 distinct queries from table history
    cur.execute("USE project2")

    select_stmt = (
     "SELECT query from history where user_id= %s order by id desc limit 15"
    )
    cur.execute(select_stmt, user_id)    
    rows = cur.fetchall();
    return [row[0] for row in rows]
