"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!

# Homepage route
@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/movies')
def all_movies():
    """ View all movies. """

    #call function from CRUD to get all movies
    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Show details on a particular movie."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route('/users')
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template('all_users.html', users=users)

@app.route('/users', methods=["POST"])
def register_user():
    """Register a new user."""

    #retrieve data from request.form
    email = request.form.get("email")
    password = request.form.get("password")
    
    #if user with this email exists:
    if (crud.get_user_by_email(email)):
        #flash a message to tell user they can't create accoun
        flash('Your account already exists!')
    #otherwise
    else:
        #create a new user
        new_user = crud.create_user(email, password)
        #add to database.
        db.session.add(new_user)
        #commit to database
        db.session.commit()
        #flash message telling them success
        flash('Success! Account created.')

    #redirect back to homepage
    return redirect('/')

@app.route('/users/<user_id>')
def show_user(user_id):
    """Show details on a particular user."""

    user = crud.get_user_by_id(user_id)
    
    return render_template('user_details.html', user=user)
    
@app.route('/login', methods=['POST'])
def login():
    """Log in a particular user."""

    #pull info from form submission
    email = request.form.get("email")
    password = request.form.get("password")

    #query for user with given email
    user = crud.get_user_by_email(email)
    #make sure password matches
    if password == user.password:
        #add primary key to flask session
        session['user'] = user.user_id
        #flash success message
        flash('Successfully logged in!')
    else:
        flash('Wrong password :(')
        return redirect('/')

    return redirect('/movies')


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
