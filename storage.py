import pickle
import os
from students import Students   # tumhari Students class yahan se import ho rahi hai,students.py

file_name = "data.pkl"

def save_student_data(student):
    students_list = []   # yahan galti thi, Students class overwrite ho rahi thi
    if os.path.exists(file_name):
        with open(file_name, "rb") as file:
            students_list = pickle.load(file)

    students_list.append(student)

    with open(file_name, "wb") as file:
        pickle.dump(students_list, file)


# Example students
s1 = Students("sameer", 123, 30)
s2 = Students("rohit", 124, 50)

save_student_data(s1)
save_student_data(s2)

def load_student_data():
    with open("data.pkl","rb") as file:
        data=pickle.load(file)
    for student in data:
        print(student.display())
load_student_data()            