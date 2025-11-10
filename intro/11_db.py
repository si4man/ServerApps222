import mysql.connector

db_ini = {
    "host": "localhost",
    "port": 3306,
    "user": "user_222",
    "password": "pass_222",
    "database": "server_222",
    "charset": "utf8mb4",
    "collation": "utf8mb4_unicode_ci",
    "use_unicode": True,
}

db_connection = None


def connect():
    global db_connection
    try:
        db_connection = mysql.connector.connect(**db_ini)
    except mysql.connector.Error as err:
        print(err)
    else:
        print("Connection OK")


def demo1():
    sql = "select current_timestamp union all select current_timestamp"
    try:
        cursor = db_connection.cursor()
        cursor.execute(sql)
    except mysql.connector.Error as err:
        print(err)
    else:
        print(cursor.column_names)
        row = next(cursor)
        print(row)
    finally:
        try:
            cursor.close()
        except:
            pass


def demo2():
    global db_connection
    sql = "select uuid() union select uuid()"
    try:
        with db_connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql)
            for row in cursor:
                print(row)
    except mysql.connector.Error as err:
        print(err)


def demo3():
    global db_connection
    sql = "select uuid(), uuid() union select uuid(), uuid()"
    try:
        with db_connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql)
            print(cursor.column_names)
            for row in cursor:
                print(row)
    except mysql.connector.Error as err:
        print(err)


def demo_par():
    global db_connection
    sql = "select datediff(current_date, %s) Days"
    try:
        with db_connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, ("2025-01-01",))
            for row in cursor:
                print(row)
    except mysql.connector.Error as err:
        print(err)


def demo_prep():
    global db_connection
    sql = "select datediff(current_date, ?) Days"
    try:
        with db_connection.cursor(dictionary=True, prepared=True) as cursor:
            cursor.execute(sql, ("2025-01-01",))
            for row in cursor:
                print(row)
            cursor.execute(sql, ("2025-10-01",))
            print(next(cursor))
    except mysql.connector.Error as err:
        print(err)


def main():
    connect()
    if db_connection is None:
        return
    # demo2()
    print("-----------------------")
    # demo3()
    # demo_par()
    demo_prep()


if __name__ == "__main__":
    main()
