"""CRUD operations/utility functions for creating data."""

from model import db, User, Movie, Rating, connect_to_db


# Functions start here!

def create_user(email, password):
    """Create and return a new user.
    
    :param: email and password are Strings that are passed during function call
    :return: a User object
    """

    user = User(email=email, password=password)

    return user


def get_users():
    """Returns all users."""

    return db.session.query(User)


def get_user_by_id(user_id):
    """Returns a user by id"""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Returns a user by email"""

    return User.query.filter(User.email == email).first()


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(
        title=title, 
        overview=overview, 
        release_date=release_date, 
        poster_path=poster_path,
        )

    return movie


def get_movies():
    """Returns all movies."""

    return db.session.query(Movie)


def get_movie_by_id(movie_id):
    """Returns a movie by id"""

    return Movie.query.get(movie_id)



def create_rating(user, movie, score):
    """Create and return a rating."""

    rating = Rating(
        user=user,
        movie=movie,
        score=score,
    )

    return rating



if __name__ == '__main__':
    from server import app
    connect_to_db(app)