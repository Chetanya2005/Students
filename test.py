import pickle

with open("data.pkl","rb") as file:
    data=pickle.load(file)
    
print(data[0].display())
print(data[1].display())    