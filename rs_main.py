# Recommendation System
import pandas as pd
import numpy as np
import warnings
####################
warnings.filterwarnings('ignore')

# Load in a tab separated dataset with \t as a separating parameter
datafile = pd.read_csv('u.data', sep='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])

# Head of data
datafile.head()

# Load in movie titles

movie_titles = pd.read_csv('Movie_Titles')
movie_titles.head()

datafile = pd.merge(datafile, movie_titles, on = 'item_id')

datafile.head()
####################
# user_id - the ID of the user who rates
# item_id - the ID of the movie
# rating - The rating the user gave the movie, 1 - 5
# timestamp - The time the movie was rated
# title - The title of the movie
####################

# describe or info commands gives a brief description of the dataset

datafile.describe()

# dataframe with average rating for each movie and the number of ratings.

ratings = pd.DataFrame(datafile.groupby('title')['rating'].mean())

ratings.head()

# number of ratings for each movie
ratings['number_of_ratings'] = datafile.groupby('title')['rating'].count()
ratings.head()

# Histogram

import matplotlib.pyplot as plt
#
ratings['rating'].hist(bins=50)

ratings['number_of_ratings'].hist(bins=60)

# Relationship between rating and number of ratings

import seaborn as sns
sns.jointplot(x='rating', y='number_of_ratings', data=ratings)