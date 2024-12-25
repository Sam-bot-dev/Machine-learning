import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
import joblib
# from sklearn.model_selection import train_test_split

# music_data= pd.read_csv("music.csv")
# x=music_data.drop(columns=['genre'])
# y=music_data['genre']
# model=DecisionTreeClassifier()
# model.fit(x,y)
model=joblib.load('music-recommeder.joblib')

predictions=model.predict([[21,1]])
print(predictions)

