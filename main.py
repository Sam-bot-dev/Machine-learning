import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
music_data=pd.read_csv('music.csv')
# print(music_data)
X=music_data.drop(columns=['genre'])
# X=music_data.loc[:, music_data.columns != 'genre']
print(X)
Y=music_data['genre']
print(Y)
model= DecisionTreeClassifier()
model.fit(X,Y)
predictions=model.predict([[21,1],[22,0]])
print(predictions)