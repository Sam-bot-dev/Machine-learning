import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
# import joblib
# from sklearn.ensemble import RandomForestClassifier
music_data=pd.read_csv('music.csv')
X=music_data.drop(columns=['genre'])
Y=music_data['genre']

model= DecisionTreeClassifier()
model.fit(X,Y)
# joblib.dump(model,"music-recommeder.joblib")
predictions=model.predict([[21,1]])
# print(predictions) 