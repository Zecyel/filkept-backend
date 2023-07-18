from sqlite3 import connect, Connection, Cursor

class ConnectionBase:

    _database_path = ''
    _conn: Connection = None

    def __init__(self):
        self._conn = connect(self._database_path, check_same_thread=False)

    def __del__(self):
        self._conn.close()

    def commit(self):
        self._conn.commit()
    
    def cursor(self):
        return self._conn.cursor()


class ORMBase:

    _connection: ConnectionBase = None
    _table_name = ''
    _cursor: Cursor = None

    def __init__(self):
        self._cursor = self._connection.cursor()
    
    def __del__(self):
        self._cursor.close()