import pandas as pd
import numpy as np

frame = pd.read_csv('rating_final.csv')
cuisine = pd.read_csv('chefmozcuisine.csv')

frame.head()
cuisine.head()

rating_count = pd.DataFrame(frame.groupby('placeID')['rating'].count())
print rating_count.head()