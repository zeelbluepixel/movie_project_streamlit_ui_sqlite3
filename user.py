from movie import movies
from dbConnetion import dbConn

class user:
    def start(self):
        while(True):
            print("=== Welcome Movie Rating ===")
            print("1. Admin")
            print("2. User")
            print("3. Exit")
            try: 
                rol = int(input("Select 1-3 only one: "))
                print("---------------------------------")
            except:
                print("add only int number 1-3!!\n")
                continue

            if rol == 1:
                pas = input("Enter Admin Password: ")

                if pas == "admin123":
                    print("\n=== Welcome Admin ===")
                    user.admin_menu(self)
                else:
                    print("Password not valid!!")
                    continue

            elif rol == 2:
                print("\n=== Welcome User ===\n")
                user.user_menu(self)
            elif rol == 3:
                print("Thank You!!")
                break
            else:
                print("add only 1-3!!\n")
                continue

    def admin_menu(self):
        while(True):
            print("---------------------------------")
            print("--- Admin Menu ---")
            print("1. Add New Movie")
            print("2. View All Movie")
            print("3. Delet Movie")
            print("4. Update Movie")
            print("5. View Only Movie & Rating")
            print("6. View Only Movie & Total Rating")
            print("7. Data Backup")
            print("8. Exit")

            try: 
                choice = int(input("Select 1-7 only one: "))
                print("---------------------------------")
            except:
                print("add only int number 1-7!!\n")
                continue

            if choice == 1:
                print("\n=== Add New Movie ===\n")
                movies.add_movie(self)
            elif choice == 2:
                 movies.view_movie(self)
            elif choice == 3:
                movies.delete_movie(self)
            elif choice == 4:
                movies.update_movie(self)
            elif choice == 5:
                movies.name_rating(self)
            elif choice == 6:
                movies.name_rating_count(self)
            elif choice == 7:
                ans = input("Enter 'y' For Data BackUp: ")
                if ans == "y":
                    dbConn.backup_moviedb(self)

            elif choice == 8:
                break
            else:
                print("add only 1-7 int value!!")
                continue

    def user_menu(self):
        while(True):
            print("\n---------------------------------")
            print("--- User Menu ---")
            print("1. View All Movie")
            print("2. Add Rating")
            print("3. View Your All Rating")
            print("4. Update Your Rating")
            print("5. View Only Movie & Rating")
            print("6. Top 5 Best Movie")
            print("7. Exit")

            try: 
                choice = int(input("Select 1-7 only one: "))
                print("---------------------------------")
            except:
                print("add only int number 1-7!!\n")
                continue

            if choice == 1:
                movies.view_movie(self)
            elif choice == 2:
                movies.add_rating(self)
            elif choice == 3:
                movies.view_all_rating(self)
            elif choice == 4:
                movies.update_rating(self)
            elif choice == 5:
                movies.name_rating(self)
            elif choice == 6:
                movies.top_5_movie(self)
            elif choice == 7:
                break
            else:
                print("add only 1-7 int value!!")
                continue

try:
    db = dbConn()
    conn = db.db()
    print("Database Connetion Done!!")

    db.table_conn()
    print("Table Created!!")

    try:
        st = user()
        st.start()

    except Exception as e:
        print("Error:",e)

except Exception as ee:
    print("Database error:",ee)