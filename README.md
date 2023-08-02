# Filkept.backend

## setup

1. 初始化数据库`user.db`，并置于`/database/data`目录下

```sql
create table user(
    userid integer primary key autoincrement,
    username string(20),
    password string(20) 
);
```

2. 在根目录执行如下指令，运行后端

```
waitress-serve --host 127.0.0.1 --port 933 main:app
```
