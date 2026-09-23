# Movie Rating System

A simple **Movie Rating System** developed using **Python, OOP, SQLite3, and Streamlit**.

The project provides a web-based user interface using Streamlit for managing movies and movie ratings.

## Roles

This project has 2 roles:

1. Admin
2. User

## Technologies Used

* Python
* Streamlit
* SQLite3
* OOP
* SQLite Database

## Database Tables

The project contains 2 main tables:

### 1. Movie

Stores movie information such as:

* Movie ID
* Movie Name
* Category
* Release Year
* Description

### 2. User Rating

Stores ratings given by users for movies.

The table stores information such as:

* Rating ID
* Movie ID
* User Name
* Rating
* Review

## Streamlit UI

The project uses **Streamlit** to create the web interface.

The Streamlit application provides:

* Sidebar navigation
* Admin login page
* User menu
* Movie management forms
* Movie tables
* Rating forms
* Rating information
* Buttons for Add, Update, and Delete operations
* Interactive movie and rating views

## Admin Features

Admin uses a **static username and password** for login.

Admin can:

* Login with username and password
* Add a movie
* Update movie details
* Delete a movie
* View all movies
* View movies with ratings
* View movie rating count
* View rating details

## User Features

Users do not require a username or password.

Users can:

* View all movies
* Add a rating to a movie
* View their previous ratings
* Update their previous rating
* View movies with ratings

## Streamlit Features Used

This project uses different Streamlit components, including:

* `st.title()`
* `st.header()`
* `st.subheader()`
* `st.write()`
* `st.text_input()`
* `st.number_input()`
* `st.selectbox()`
* `st.text_area()`
* `st.button()`
* `st.radio()`
* `st.sidebar`
* `st.table()`
* `st.dataframe()`
* `st.success()`
* `st.error()`
* `st.warning()`
* `st.session_state`

## Project Structure

```text
Movie/
│
├── app.py
├── dbConnection.py
├── admin.py
├── user.py
├── movie.db
├── README.md
└── Readme.txt
```

## File Description

| File              | Description                                          |
| ----------------- | ---------------------------------------------------- |
| `app.py`          | Main Streamlit application                           |
| `dbConnection.py` | Connects Python with SQLite3 database                |
| `admin.py`        | Contains admin login and movie management operations |
| `user.py`         | Contains user rating and movie operations            |
| `movie.db`        | SQLite3 database                                     |
| `README.md`       | Project documentation                                |
| `Readme.txt`      | Simple project information                           |

## Application Flow

```text
                    Movie Rating System
                            │
                            ▼
                    Streamlit UI
                            │
                ┌───────────┴───────────┐
                │                       │
              Admin                   User
                │                       │
                ▼                       ▼
            Login Required        No Login Required
                │                       │
                ▼                       ▼
        Admin Dashboard          User Dashboard
                │                       │
        ┌───────┼────────┐       ┌──────┼─────────┐
        │       │        │       │      │         │
       Add    Update   Delete   View   Rating   My Ratings
     Movie    Movie    Movie   Movies  Movie    / Update
                │                       │
                └───────────┬───────────┘
                            ▼
                       SQLite3
                        Database
```

## How to Run

### 1. Open the Project Folder

Open the project folder:

```text
Movie/
```

### 2. Install Required Packages

Install Streamlit using:

```bash
pip install streamlit
```

SQLite3 is included with Python, so no separate installation is normally required.

### 3. Run the Streamlit Application

Run the main application file:

```bash
streamlit run app.py
```

### 4. Open the Application

After running the command, Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open this URL in your web browser.

## Admin Login

Admin login uses a fixed username and password defined in the Python code.

After successful login, the Admin Dashboard is displayed.

Admin can manage movies and view movie rating information from the Streamlit interface.

## User

Users do not need to create an account or login.

After selecting the User role, users can access the User Dashboard.

Users can:

* View movies
* Give ratings
* View their ratings
* Update their ratings
* View movie ratings

## Database

The project uses **SQLite3**, so no separate database server is required.

The database file is:

```text
movie.db
```

Python communicates with the SQLite database using the built-in `sqlite3` module.

## Main Features

```text
Movie Rating System
│
├── Streamlit UI
│
├── Admin
│   ├── Login
│   ├── Add Movie
│   ├── Update Movie
│   ├── Delete Movie
│   ├── View Movies
│   ├── View Movie Ratings
│   ├── View Rating Details
│   └── View Rating Count
│
└── User
    ├── View Movies
    ├── Add Rating
    ├── View My Ratings
    ├── Update Rating
    └── View Movie Ratings
```

## OOP Implementation

The project uses **Object-Oriented Programming (OOP)** to organize the application logic.

Classes can be used for:

* Database connection
* Movie operations
* Admin operations
* User operations
* Rating operations

This makes the project easier to maintain and organize.

## Streamlit Session State

The project uses:

```python
st.session_state
```

to maintain information between Streamlit reruns.

For example, it can store:

* Admin login status
* Selected role
* Current user name
* Current page/menu

Example:

```python
if "admin_login" not in st.session_state:
    st.session_state.admin_login = False
```

## Advantages of Streamlit Version

Compared with a normal console application, the Streamlit version provides:

* Web-based user interface
* Interactive forms
* Buttons and menus
* Tables for displaying database records
* Easy navigation
* No HTML/CSS/JavaScript required
* Direct integration with Python

## Conclusion

This project demonstrates a simple **Movie Rating System** using **Python, OOP, SQLite3, and Streamlit**.

The application provides separate **Admin and User roles** with a web-based Streamlit interface. Admins can manage movies and view rating information, while users can view movies and add or update their ratings.

The project is useful for understanding how **Python, OOP, SQLite3, database operations, and Streamlit UI** can be combined to create a complete database-driven application.
