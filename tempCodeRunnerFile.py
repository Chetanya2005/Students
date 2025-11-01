import pickle
import os
from students import Students
file_name="data.pkl"

def save_student_data(student):
    Students=[]
    if os.path.exists(file_name):
        with open("data.pkl","rb") as file:
            Students=pickle.load(file)
    Students.append(student)
    with open("data.pkl","wb") as file:
        pickle.dump(Students,file)
        
s1=Students("sameer",123,30)
s2=Students("rohit",124,50)
save_student_data(s1)
save_student_data(s2)