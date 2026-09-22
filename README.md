# Movie Rating System

A simple **Movie Rating System** developed using **Python** and **SQLite3**.

## Roles

This project has 2 roles:

1. Admin
2. User

## Technologies Used

* Python
* SQLite3
* OOP
* SQLite Database

## Database Tables

The project contains 2 main tables:

### 1. Movie

Stores movie information.

### 2. User Rating

Stores user ratings for movies.

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
* View movie rating details

## User Features

Users do not require username or password.

Users can:

* View all movies
* Add a rating to a movie
* View their previous ratings
* Update their previous rating
* View movies with ratings

## Project Structure

```text
Movie/
│
├── dbConnetion.py
├── movie.py
├── user.py
├── movie.db
├── README.md
└── Readme.txt
```

## File Description

| File             | Description                                           |
| ---------------- | ----------------------------------------------------- |
| `dbConnetion.py` | Connects Python with SQLite3 database                 |
| `movie.py`       | Contains movie-related operations and admin functions |
| `user.py`        | Contains user-related operations and rating functions |
| `movie.db`       | SQLite3 database                                      |
| `README.md`      | Project documentation                                 |
| `Readme.txt`     | Simple project information                            |

## How to Run

### 1. Open the project folder

```text
Movie/
```

### 2. Run the main Python file

For example:

```bash
python movie.py
```

or

```bash
python user.py
```

### 3. Select the required role

* Admin
* User

## Admin Login

Admin login uses a fixed username and password defined in the Python code.

Users do not need to create an account or login.

## Database

The project uses SQLite3, so no separate database server is required.

The database file is:

```text
movie.db
```

## Main Features

```text
Admin
 ├── Login
 ├── Add Movie
 ├── Update Movie
 ├── Delete Movie
 ├── View Movies
 ├── View Movie Ratings
 └── View Rating Count

User
 ├── View Movies
 ├── Add Rating
 ├── View My Ratings
 ├── Update Rating
 └── View Movie Ratings
```

## Conclusion

This project demonstrates a simple **Movie Rating System** using Python, OOP, and SQLite3 with separate Admin and User roles.
