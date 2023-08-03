from sqlite3 import Cursor
from .base import Connection, context

EbookConnection = Connection('database/data/ebook.db')

class EbookORM:

    @context(EbookConnection)
    def upload(cur: Cursor, self, userid: int, remote_url: str, name: str, description: str) -> bool:
        cur.execute('insert into book (userid, url, bookname, description) values (?, ?, ?, ?)',
                    (userid, remote_url, name, description))
        return 'ok'

