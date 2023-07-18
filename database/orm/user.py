from .base import ConnectionBase, ORMBase

class UserConnection(ConnectionBase):
    _database_path = 'database/data/user.db'

UserConnectionSingleton = UserConnection()

class UserORM(ORMBase):
    _table_name = 'user'
    _connection = UserConnectionSingleton

    def login(self, username: str, password: str) -> bool:
        self._cursor.execute('select * from user where username == ? and password == ?',
                              (username, password))
        return len(self._cursor.fetchall()) == 1

UserORMSingleton = UserORM()