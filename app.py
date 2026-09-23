import streamlit as st
from admin import Admin
from user import User


class Start:

    def start_app(self):
        try:
            st.title("Welcome Movie Rating")
            st.header("Login")

            rol = st.selectbox("Select Role",["Select Your Role","1. Admin","2. User"])

            if rol == "1. Admin":

                name = st.text_input("Enter User Name")
                password = st.text_input("Enter Password",type="password")

                if st.button("Submit"):
                    if name in ["a", "admin", "Admin", "A"]:
                        if password in ["a","admin","Admin","A","admin123","Admin123"]:
                            st.session_state.page = "Admin_rol"
                            st.rerun()
                        else:
                            st.error("Password is Invalid")
                    else:
                        st.error("Username is Invalid")

            elif rol == "2. User":
                st.session_state.page = "User_rol"
                st.success("Welcome User!!")
                st.rerun()

        except Exception as e:
            st.error("Login Error: " + str(e))

try:
    if "page" not in st.session_state:
        st.session_state.page = "login"

    if st.session_state.page == "login":
        o = Start()
        o.start_app()

    elif st.session_state.page == "Admin_rol":
        o1 = Admin()
        o1.admin_menu()

    elif st.session_state.page == "User_rol":
        o2 = User()
        o2.user_menu()

except Exception as e:
    st.error("Application Error: " + str(e))