import pymysql


class DBConnector:
    def __init__(self, host='localhost', port=3306, user='root', passwd='pythoncourse', db='my_db'):
        self.db = db
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db)

    def __del__(self):
        self.conn.close()  # Close connection when object is destroyed

    def put_user(self, user_id, new_name):
        with self.conn.cursor() as cursor:  # Use context manager for cursor
            cursor.execute("UPDATE users SET user_name = %s WHERE user_id = %s",
                           (new_name, user_id))  # Prepared statement
        self.conn.commit()

    def add_user(self, user_id, user_name):
        with self.conn.cursor() as cursor:
            cursor.execute("INSERT INTO users (user_name, user_id) VALUES (%s, %s)",
                           (user_name, user_id))  # Prepared statement
            self.conn.commit()
            num_affected_rows = cursor.rowcount
            if num_affected_rows > 0:
                return 200

    def select_id(self, user_id):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT user_name FROM users WHERE user_id = %s", (user_id,))
            result = cursor.fetchone()
        return result[0]  # Assuming a single result is expected

    def delete_user(self, user_id):
        with self.conn.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        self.conn.commit()
        return 200
