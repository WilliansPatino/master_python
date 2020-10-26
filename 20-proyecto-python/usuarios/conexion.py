import mariadb

def conectar():
    db = mariadb.connect(
        host='192.168.250.8',
        user='root',
        port=3306,
        passwd='BUka7Zz7oZ',
        database='master_python'
    )

    cur = db.cursor(buffered=True)

    return [db, cur]


