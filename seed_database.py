"""Script to seed database. No functions defined here."""

import os
import json
from random import choice, randint
from datetime import datetime

import model
import server
import crud

# Tells Python to run the dropdb command using os.system
os.system("dropdb ratings")
# Tells Python to run the createdb command using os.system
os.system('createdb ratings')

# Connect to the database to the server
model.connect_to_db(server.app)
# Create the tables
model.db.create_all()

# Open and read the following JSON file as 'f'
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    # TODO: get the title, overview, and poster_path from the movie
    title = movie['title']
    overview = movie['overview']
    poster_path = movie['poster_path']
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    release_date = datetime.strptime(movie['release_date'], "%Y-%m-%d")

    # TODO: create a movie here and append it to movies_in_db
    my_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(my_movie)

model.db.session.add_all(movies_in_db)
# model.db.session.commit()

#Create users, store them in list so we can use them
for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'
    print('user created!')

    # TODO: create a user here
    my_user = crud.create_user(email, password)
    model.db.session.add(my_user)

    # TODO: create 10 ratings for the user
    for n in range(10):
        my_rating = crud.create_rating(my_user, choice(movies_in_db), randint(1,5))
        model.db.session.add(my_rating)
        print('rating added!')

# Commit everything to the database
model.db.session.commit()