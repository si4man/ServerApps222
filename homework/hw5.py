import mysql.connector
from datetime import datetime

db_config = {
    "host": "localhost",
    "port": 3306,
    "user": "user_222",
    "password": "pass_222",
    "database": "server_222",
    "charset": "utf8mb4",
    "collation": "utf8mb4_unicode_ci",
    "use_unicode": True,
    "autocommit": True,
}

db_conn = None

def connect():
    global db_conn
    try:
        db_conn = mysql.connector.connect(**db_config)
        print("Database connection established.")
    except mysql.connector.Error as err:
        print(f"Connection error: {err}")
        db_conn = None

def input_date():
    while True:
        text = input("Enter a date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Invalid format, please try again.")

def check_date(date_str):
    sql = "SELECT DATEDIFF(CURRENT_DATE, %s) AS diff"
    try:
        with db_conn.cursor(dictionary=True) as cursor:
            cursor.execute(sql, (date_str,))
            row = next(cursor)
            diff = row["diff"]
            if diff == 0:
                print("The date is today.")
            elif diff > 0:
                print(f"The date was {diff} day{'s' if diff > 1 else ''} ago.")
            else:
                print(f"The date is in {abs(diff)} day{'s' if abs(diff) > 1 else ''}.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")

def main():
    connect()
    if not db_conn or not db_conn.is_connected():
        return
    date_str = input_date()
    check_date(date_str)
    db_conn.close()

if __name__ == "__main__":
    main()
