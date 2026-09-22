from dbConnetion import dbConn

class movies:

    def add_movie(self):
        movieName = input("Enter Movie Name: ")
        movieType = input("Enter Movie Type: ")
        movieRelDate = input("Enter Movie Release Date: ")
        rating = 0
        ratingCount = 0

        db = dbConn()
        conn = db.db()
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO movie(m_name,m_type,rel_date,rating,number_of_rating)
        VALUES (?,?,?,?,?)''',(movieName,movieType,movieRelDate,rating,ratingCount))

        print("\nMovie Added!!")
        print("---------------------------------")

        conn.commit()
        conn.close()

    def view_movie(self):
        db = dbConn()
        conn = db.db()
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM movie''')

        result = cursor.fetchall()
        print("------------------------------------------------------------------------------------------------------------")
        print("ID","|","MOVIE NAME","|","MOVIE TYPE","|","RELEASE DATE","|","RATING","|","TOTAL RATING","|","CREATED AT","|")
        print("------------------------------------------------------------------------------------------------------------")
        for i in range(len(result)):
            for j in result[i]:
                print(j,end=" | ")
            print()

        conn.commit()
        conn.close()

    def delete_movie(self):
        movies.view_movie(self)

        db = dbConn()
        conn = db.db()
        cursor = conn.cursor()

        try:
            del_id = int(input("Enter ID For Movie Delete:"))
            cursor.execute("DELETE FROM movie WHERE m_id = ?",(del_id,))
            print("\nDeleted Movie!!")
            print()

            conn.commit()
            conn.close()
        except:
            print("Add Int Value Only!!")
            movies.delete_movie(self)
    
    def update_movie(self):
        while(True):
            movies.view_movie(self)
            print("\n---------------------------------")
            print("--- Select One To Update ---")
            print("1. Name")
            print("2. Type")
            print("3. Release Date")
            print("4. Exit")

            try: 
                choice = int(input("Select 1-4 only one: "))
                print("---------------------------------")
            except:
                print("add only int number 1-4!!\n")
                continue

            if choice == 1:
                up_data = "m_name"
                row = "Movie Name"
            elif choice == 2:
                up_data = "m_type"
                row = "Movie Type"
            elif choice == 3:
                up_data = "rel_date"
                row = "Release Date"
            elif choice == 4:
                break
            else:
                print("Enter Only 1 to 4!!")
                continue

            db = dbConn()
            conn = db.db()
            cursor = conn.cursor()

            addid = int(input("Enter Id For Upadte: "))
            update = input(f"Enter {row}: ")
            cursor.execute(f"UPDATE movie SET {up_data} = ? WHERE m_id = ?",(update,addid))

            print()
            print(f"{row} Updated!!")
            print()

            conn.commit()
            conn.close()

    def name_rating(self):
        db = dbConn()
        conn = db.db()
        cursor = conn.cursor()

        cursor.execute('''SELECT m_name,rating FROM movie''')

        result = cursor.fetchall()
        print("---------------------------")
        print("MOVIE NAME","|","RATING","|")
        print("---------------------------")
        for i in range(len(result)):
            for j in result[i]:
                print(j,end=" | ")
            print()

        conn.commit()
        conn.close()
        print()

    def name_rating_count(self):
        db = dbConn()
        conn = db.db()
        cursor = conn.cursor()

        cursor.execute('''SELECT m_name,rating,number_of_rating FROM movie''')

        result = cursor.fetchall()
        print("-----------------------------------------------")
        print("MOVIE NAME","|","RATING","|","TOTAL RATING","|")
        print("-----------------------------------------------")
        for i in range(len(result)):
            for j in result[i]:
                print(j,end=" | ")
            print()

        conn.commit()
        conn.close()
        print()

    def add_rating(self):
        uName = input("Enter Name:")
        movies.view_movie(self)

        movie_id = int(input("Enter Movie Id You Add Rating: "))
        while True:
            try:
                rating = float(input("Enter (1-10) Rating: "))
                if rating > 10 or rating < 0:
                    print("add only 0 to 10 num !!")
                    continue
                else:
                    break
            except:
                print("only 0 to 10 num!!")
                continue

        db = dbConn()
        conn = db.db()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO user (m_id,u_name,rating) VALUES (?,?,?)",(movie_id,uName,rating))

        cursor.execute("SELECT rating,number_of_rating FROM movie WHERE m_id = ?",(movie_id,))
        rate = cursor.fetchone()

        temp = []
        for i in rate:
            temp.append(i)

        if int(temp[0]) == 0:
            update_rating = rating
        else:
            update_rating = (int(temp[0])+rating)/2

        cursor.execute("UPDATE movie SET rating = ?,number_of_rating = number_of_rating + 1 WHERE m_id = ?",(update_rating,movie_id))

        print("Rating Added!!")
        print()

        conn.commit()
        conn.close()


    def update_rating(self):
        db = dbConn()
        conn = db.db()
        cursor = conn.cursor()

        uName = input("Enter Name:")
        movies.view_movie(self)

        print("\n=== Your Rating ===\n")
        cursor.execute("select u.u_name,m.m_id,u.rating,m.rating from user as u join movie as m on u.m_id=m.m_id")

        result = cursor.fetchall()
        temp = list(result[0])

        if uName == temp[0]:
            print("------------------------------------------------------------------------------------------------------------")
            print("USER NAME","|","MOVIE ID","|","USER RATIND","|","RATING","|","RATING","|")
            print("------------------------------------------------------------------------------------------------------------")

            x = []
            c = 1

            for i in range(len(result)):
                for j in result[i]:
                    t = result[i]
                    if t[0] == uName:
                        x.append(j)
            for i in x:
                if c == 4:
                    print(i," |")
                    c=1
                else:
                    print(i,end=" | ")
                    c+=1
            print()
            movie_id = int(input("Enter Movie Id You Update Rating: "))
            while True:
                try:
                    rating = float(input("Enter (1-10) Rating: "))
                    if rating > 10 and rating < 0:
                        print("add only 0 to 10 num !!")
                        continue
                    else:
                        break
                except:
                    print("only 0 to 10 num!!")
                    continue

            cursor.execute("UPDATE user SET rating = ? WHERE m_id = ?",(rating,movie_id))

            conn.commit()

            cursor.execute("SELECT rating,number_of_rating FROM movie WHERE m_id = ?",(movie_id,))
            rate = cursor.fetchone()

            temp = []
            for i in rate:
                temp.append(i)

            if int(temp[0]) == 0:
                update_rating = rating
            else:
                update_rating = (int(temp[0])+rating)/2

            conn.commit()

            cursor.execute("UPDATE movie SET rating = ? WHERE m_id = ?",(update_rating,movie_id))

            print("Rating Added!!")
            print()

            conn.commit()
            conn.close()
        else:
            print("Not User Found!!")

        


    def view_all_rating(self):
        name = input("Enter Your Name: ")

        db = dbConn()
        conn = db.db()
        cursor = conn.cursor()

        cursor.execute("select u.u_name,m.m_name,u.rating,m.rating from user as u join movie as m on u.m_id=m.m_id")

        result = cursor.fetchall()
        temp = list(result[0])

        if name == temp[0]:
            print("------------------------------------------------------------------------------------------------------------")
            print("USER NAME","|","MOVIE NAME","|","USER RATIND","|","RATING","|","RATING","|")
            print("------------------------------------------------------------------------------------------------------------")

            x = []
            c = 1

            for i in range(len(result)):
                for j in result[i]:
                    t = result[i]
                    if t[0] == name:
                        x.append(j)
            for i in x:
                if c == 4:
                    print(i," |")
                    c=1
                else:
                    print(i,end=" | ")
                    c+=1                        
            print()
        else:
            print("Not User Found!!")

        conn.commit()
        conn.close()

    def top_5_movie(self):
        db = dbConn()
        conn = db.db()
        cursor = conn.cursor()

        print("\n=== Top 5 Movie ===")
        cursor.execute('''SELECT * FROM movie ORDER BY rating DESC limit 5''')

        result = cursor.fetchall()
        print("------------------------------------------------------------------------------------------------------------")
        print("ID","|","MOVIE NAME","|","MOVIE TYPE","|","RELEASE DATE","|","RATING","|","TOTAL RATING","|","CREATED AT","|")
        print("------------------------------------------------------------------------------------------------------------")
        for i in range(len(result)):
            for j in result[i]:
                print(j,end=" | ")
            print()

        conn.commit()
        conn.close()