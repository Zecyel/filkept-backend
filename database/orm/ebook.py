from sqlite3 import Cursor
from .base import Connection, context

EbookConnection = Connection('database/data/ebook.db')

class EbookORM:

    @context(EbookConnection)
    def upload(cur: Cursor, self, userid: int, remote_url: str, name: str, description: str) -> bool:
        cur.execute('insert into book (userid, url, bookname, description) values (?, ?, ?, ?)',
                    (userid, remote_url, name, description))
        EbookConnection.commit()
        return 'ok'

    @context(EbookConnection)
    def list(cur: Cursor, self, userid: int) -> list:
        cur.execute('select bookname, description, url, bookid from book where userid = ?', (userid, ))
        return [{
            'name': i[0],
            'description': i[1],
            'url': i[2],
            'id': i[3]
        } for i in cur.fetchall()]

    @context(EbookConnection)
    def info(cur: Cursor, self, bookid: int) -> dict:
        cur.execute('select * from book where bookid = ?', (bookid, ))
        ret = cur.fetchone()
        return {
            'name': ret[3],
            'userid': ret[1],
            'url': ret[2],
            'description': ret[4]
        }
