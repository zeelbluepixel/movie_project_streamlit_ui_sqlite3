import sqlite3

class dbConn:

    def db(self):
        conn = sqlite3.connect("movie.db")
        return conn

    def table_conn(self):

        db = dbConn()
        conn = db.db()
        cursor = conn.cursor()

        movie_sql = '''CREATE TABLE IF NOT EXISTS movie(
                    m_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    m_name varchar(50) NOT NULL,
                    m_type varchar(30),
                    rel_date DATE,
                    rating DECIMAL(10,2),
                    number_of_rating INT,
                    createat TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )'''
        cursor.execute(movie_sql)

        user_sql = '''CREATE TABLE IF NOT EXISTS user(
                    u_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    m_id INT ,
                    u_name varchar(50),
                    rating DECIMAL(10,2),
                    createat TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (m_id) REFERENCES movie(m_id)
                    )'''
        cursor.execute(user_sql)

        conn.commit()
        conn.close()

    def backup_moviedb(self):

        db = dbConn()
        conn = db.db()
        cursor = conn.cursor()


        backup_table = sqlite3.connect("back_movie.db")
        conn.backup(backup_table)
        # print("Data BackUp Successfully Done!!")

        conn.commit()
        conn.close()