# Recommendation System
import pandas as pd
import numpy as np
import warnings
####################
warnings.filterwarnings('ignore')

# Load in a tab serperated dataset with \t as a seperating parameter
datafile = pd.read_csv('u.data', sep = '\t', names = ['user_id', 'item_id', 'rating', 'titmestamp'])

# Head of data
datafile.head()

# Load in movie titles

movie_titles = pd.read_csv('Movie_Titles')
movie_titles.head()
