from sqlite3 import Cursor
from .base import Connection, context

UserConnection = Connection('database/data/user.db')

class UserORM:

    @context(UserConnection)
    def login(cur: Cursor, self, username: str, password: str) -> bool:
        cur.execute('select * from user where username == ? and password == ?',
                    (username, password))
        return len(cur.fetchall()) == 1

    @context(UserConnection)
    def register(cur: Cursor, self, username: str, password: str) -> bool:
        cur.execute('select COUNT(*) from user where username == ?', (username, ))
        if cur.fetchone()[0] != 0:
            return False
        cur.execute('insert into user (username, password) values (?, ?)',
                             (username, password))
        UserConnection.commit()
        return True

    @context(UserConnection)
    def get_userid(cur: Cursor, self, username: str) -> int:
        cur.execute('select userid from user where username == ?', (username, ))
        return cur.fetchone()[0]