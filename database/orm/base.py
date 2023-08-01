from sqlite3 import connect

class Connection:

    def __init__(self, path: str) -> None:
        self._conn = connect(path, check_same_thread=False)

    def __del__(self) -> None:
        self._conn.close()
    
    def commit(self):
        self._conn.commit()

    def cursor(self):
        return self._conn.cursor()

def context(c: Connection):
    def decorator(func):
        def wrapper(*args, **kwargs):
            cur = c.cursor()
            ret = func(cur, *args, **kwargs)
            cur.close()
            return ret
        return wrapper
    return decorator