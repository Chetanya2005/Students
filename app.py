from storage import save_student_data,load_student_data
from students import Students

def Menu():
    while True:
        user_input=input('''
                         1. press 1 for data entry
                         2. press 2 for data view
                         3. press 3 for exit''')
        if user_input=="1":
            name=input("nam btaao: ")
            roll_no=input("Roll number kya hai: ")
            mark=int(input("Number btaao:"))
            
            student = Students(name,roll_no,mark) 
            save_student_data(student)
        elif user_input=="2":
            load_student_data()
        elif user_input=="3":
            break
        
Menu()        
               
#tnkir=GUI
#search by marks1
               