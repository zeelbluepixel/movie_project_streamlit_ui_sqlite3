import streamlit as st
from dbConnetion import dbConn


class Admin:

    def admin_menu(self):
            try:
                st.sidebar.title("Admin Penal")
                menu = st.sidebar.radio("Admin Menu",["Select one", "Add Movie", "View All Movie","Update Movie", "Delete Movie","View Only Movie, Rating & Rating Count","Logout"])
                if menu == "Select one":
                    Admin.home(self)
                elif menu == "Add Movie":
                    Admin.add_movie(self)
                elif menu == "View All Movie":
                    Admin.view_all_movie(self)
                elif menu == "Update Movie":
                    Admin.update_movie(self)
                elif menu == "Delete Movie":
                    Admin.delete_movie(self)
                elif menu == "View Only Movie, Rating & Rating Count":
                    Admin.view_movie_rating(self)
                elif menu == "Logout":
                    st.session_state.page = "login"
                    st.rerun()
        
            except Exception as e:
                st.error("Admin Menu Error:" + str(e))

    def home(self):
        st.title("Admin Dashboard")
        st.subheader("Welcome Admin!!")
        st.write("This is Admin Home Page")
        

    def add_movie(self):
        try:
            st.title("Add Movie")
            st.subheader("Enter Movie Detilis:")
            movieName = st.text_input("Enter Movie Name: ")
            category = st.selectbox(
                        "Movie Category",
                        ["Select One","Action", "Comedy", "Drama", "Horror", "Romance", "Thriller", "Sci-Fi"]
                    )
            movieRelDate = st.date_input("Enter Movie Release Date: ")
            rating = 0
            ratingCount = 0

            if st.button("Submit"):

                db = dbConn()
                conn = db.db()
                cursor = conn.cursor()

                cursor.execute('''INSERT INTO movie(m_name,m_type,rel_date,rating,number_of_rating)
                VALUES (?,?,?,?,?)''',(movieName,category,movieRelDate,rating,ratingCount))


                conn.commit()
                conn.close()
                st.success("---- Movie Add ----")

            
        except Exception as e:
            st.error("Movie Add Error:" + str(e))

    def view_all_movie(self):
        try:
            st.title("View All Movie")
            db = dbConn()
            conn = db.db()
            cursor = conn.cursor()

            cursor.execute('''SELECT * FROM movie''')
            result = cursor.fetchall()
            x = []

            for i in result:
                f = list(i)
                x.append(f)
            id = []
            name = []
            type = []
            reDate = []
            rating = []
            count = []
            time = []

            for i in x:
                id.append(i[0])
                name.append(i[1])
                type.append(i[2])
                reDate.append(i[3])
                rating.append(i[4])
                count.append(i[5])
                time.append(i[6])


            col = {"ID" : id,"MOVIE NAME" : name,"MOVIE TYPE" : type,"RELEASE DATE" : reDate,"RATING" : rating,"TOTAL RATING" : count,"CREATED AT": time}
            
            st.table(col)

            conn.commit()
            conn.close()
            
        except Exception as e:
            st.error("Movie Fetch Error:" + str(e))

    def update_movie(self):
        Admin.view_all_movie(self)
        st.subheader("Select One To Update")

        choice = st.radio("Select One:",["Name","Type","Release Date","Exit"])

        if choice == "Name":
            up_data = "m_name"
            row = "Movie Name"

        elif choice == "Type":
            up_data = "m_type"
            row = "Movie Type"

        elif choice == "Release Date":
            up_data = "rel_date"
            row = "Release Date"

        else:
            return

        addid = st.number_input("Enter ID For Update:",step=1)
        update = st.text_input("Enter " + row)

        if st.button("Update"):
            db = dbConn()
            conn = db.db()
            cursor = conn.cursor()

            cursor.execute(f"UPDATE movie SET {up_data} = ? WHERE m_id = ?",(update, addid))

            conn.commit()
            conn.close()

            st.success(row + " Updated!!")
            st.rerun()

    def delete_movie(self):
        st.title("Delete Movie")
        Admin.view_all_movie(self)
        db = dbConn()
        conn = db.db()
        cursor = conn.cursor()

        try:
            del_id = st.number_input("Enter ID For Movie Delete:",step=1)
            if st.button("Submit"):
                cursor.execute("DELETE FROM movie WHERE m_id = ?",(del_id,))
                conn.commit()
                conn.close()

                st.success("Deleted Movie!!")
                st.rerun()

        except:
            st.success("Add Int Value Only!!")

    def view_movie_rating(self):
        try:
            st.title("View Movie Name, Rating & Rating Count")
            db = dbConn()
            conn = db.db()
            cursor = conn.cursor()

            cursor.execute('''SELECT m_name,rating,number_of_rating FROM movie''')
            result = cursor.fetchall()
            x = []

            for i in result:
                f = list(i)
                x.append(f)
            name = []
            rating = []
            count = []

            for i in x:
                name.append(i[0])
                rating.append(i[1])
                count.append(i[2])

            col = {"MOVIE NAME" : name,"RATING" : rating,"TOTAL RATING" : count}
            st.table(col)

            conn.commit()
            conn.close()
            
            
        except Exception as e:
            st.error("Movie Fetch Error:" + str(e))
      