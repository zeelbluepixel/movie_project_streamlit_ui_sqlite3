import streamlit as st
from dbConnetion import dbConn
from admin import Admin

class User:
    def user_menu(self):
        try:
            st.sidebar.title("User Penal")
            menu = st.sidebar.radio("User Menu",["Select one", "View All Movie","Add Rating","Update Rating", "View Your Rating","View Only Movie, Rating & Rating Count","Logout"])
            if menu == "Select one":
                User.home(self)
            elif menu == "View All Movie":
                Admin.view_all_movie(self)
            elif menu == "Add Rating":
                st.title("Add Rating")
                User.add_rating(self)
            elif menu == "Update Rating":
                st.title("Update Rating")
                User.update_rating(self)
            elif menu == "View Your Rating":
                st.title("View Your Rating")
                User.view_your_rating(self)
            elif menu == "View Only Movie, Rating & Rating Count":
                Admin.view_movie_rating(self)
            elif menu == "Logout":
                st.session_state.page = "login"
                st.rerun()
    
        except Exception as e:
            st.error("Admin Menu Error:" + str(e))

    def home(self):
        st.title("User Dashboard")
        st.subheader("Welcome User")
        st.write("This is User Home Page!!")

    def add_rating(self):
        Admin.view_all_movie(self)

        uName = st.text_input("Enter Name:")

        movie_id = st.number_input("Enter Movie Id You Add Rating: ",step = 1)
        rating = st.number_input("Enter (1-10) Rating: ",value=0.0)
        if rating > 10.0 or rating < 0.0:
            st.error("add only 0 to 10 num !!")
        else:
            if st.button("Submit"):
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


                conn.commit()
                conn.close()
                st.success("Rating Added!!")
                st.rerun()

    def view_your_rating(self):
        db = dbConn()
        conn = db.db()
        cursor = conn.cursor()

        cursor.execute("SELECT u_name FROM user")
        user = cursor.fetchall()

        z = []
        for i in user:
            z.append(list(i))


        q = []
        for i in z:
            q.append(i[0])
        q = set(q)
        q = list(q)
        name = st.selectbox("Select Your Name",["Select Name"] + q)

        cursor.execute("select u.u_id,u.u_name,m.m_id,m.m_name,u.rating,m.rating from user as u join movie as m on u.m_id=m.m_id")

        result = cursor.fetchall()

        x = []
        for i in result:
            f = list(i)
            x.append(f)

        id = []
        u_name = []
        m_id = []
        m_name = []
        u_rating = []
        m_rating = []

        for i in x:
            if i[1] == name:
                id.append(i[0])
                u_name.append(i[1])
                m_id.append(i[2])
                m_name.append(i[3])
                u_rating.append(i[4])
                m_rating.append(i[5])

        col = {"Rating ID" : id,"USER NAME" : u_name,"MOVIE ID" : m_id,"MOVIE NAME" : m_name,"USER RATING" : u_rating,"MOVIE RATING" : m_rating}
        
        st.table(col)

        conn.commit()
        conn.close()

    def update_rating(self):
        User.view_your_rating(self)

        rating_id = st.number_input("Enter Rating Id You Update Rating : ",step = 1)
        rating = st.number_input("Enter (1-10) Rating: ",value=0.0)
        if rating > 10.0 or rating < 0.0:
            st.error("add only 0 to 10 num !!")
        else:
            if st.button("Submit"):
                db = dbConn()
                conn = db.db()
                cursor = conn.cursor()

                cursor.execute("UPDATE user SET rating = ? WHERE u_id = ?",(rating,rating_id))
                
                conn.commit()
                cursor.execute("SELECT m_id FROM user WHERE u_id = ?",(rating_id,))
                mo_id = cursor.fetchone()
                movie_id = list(mo_id)
    
                cursor.execute("SELECT rating,number_of_rating FROM movie WHERE m_id = ?",(movie_id[0],))
                rate = cursor.fetchone()
    
                temp = []
                for i in rate:
                    temp.append(i)
    
                if int(temp[0]) == 0:
                    update_rating = rating
                else:
                    update_rating = (int(temp[0])+rating)/2
    
                conn.commit()
    
                cursor.execute("UPDATE movie SET rating = ? WHERE m_id = ?",(update_rating,movie_id[0]))
    
                st.success("Rating Added!!")
    
                conn.commit()
                conn.close()
                st.rerun()
