from .base import ConnectionBase, ORMBase

class UserConnection(ConnectionBase):
    _database_path = 'database/data/user.db'

class UserORM(ORMBase):

    def login(self, username: str, password: str) -> bool:
        self._cursor.execute('select * from user where username == ? and password == ?',
                              (username, password))
        return len(self._cursor.fetchall()) == 1

    def register(self, username: str, password: str) -> bool:
        self._cursor.execute('select COUNT(*) from user where username == ?', (username, ))
        if self._cursor.fetchone()[0] != 0:
            return False
        self._cursor.execute('insert into user (username, password) values (?, ?)',
                             (username, password))
        self._connection.commit()
        return True
