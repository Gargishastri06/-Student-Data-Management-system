#data management 

from tabulate import tabulate

name_s=''
standard=''
date_of_addmition=''
paid=0
mark=0
due=0

def create_record(name_s,standard,date_of_addmition,fees):
    data={}
    data={'name':[name_s],'standard':[standard], 'date_of_addmition':[date_of_addmition],'paid':[paid]}
    data1=[name_s,standard,date_of_addmition,paid]
    header=['name','standard', 'date_of_addmition','paid']
    table=tabulate([data1],headers=header,tablefmt='grid')
    f=open('myfile1.txt','a')
    f.write(table)
    f.write('\n')
    f.close()
    return table


#to change the name 
def name_change(new_name):
    global name_s
    name_s=new_name
    data={}
    data={'name':name_s,'standard':standard, 'date_of_addmition':date_of_addmition,'paid':paid}
    update_data=data['name']=new_name
    data2=[update_data,standard,date_of_addmition,paid]
    header=['name','standard', 'date_of_addmition','paid']
    table=tabulate([data2],headers=header,tablefmt='grid')
    f=open('myfile1.txt','a')
    f.write(table)
    f.close()
    return table
    

#to change the standard
def standard_change(new_standard):
    global standard
    standard=new_standard
    data={}
    data={'name':name_s,'standard':standard, 'date_of_addmition':date_of_addmition,'paid':paid}
    replace_standard=data['standard']=new_standard
    data3=[name_s,standard,date_of_addmition,paid]
    header=['name','standard', 'date_of_addmition','paid']
    table=tabulate([data3],headers=header,tablefmt='grid')
    f=open('myfile1.txt','a')
    f.write(table)
    f.close()
    return table
   


#to enter the marks 
def marks(mark,total_marks,name_s):
    data={}
    data={'name':[name_s],'standard':[standard], 'date_of_addmition':[date_of_addmition],'paid':[paid],'marks':[mark]}
    s=print(f"{name_s}:{mark}/{total_marks}")
    data4=[name_s,standard,date_of_addmition,paid,mark]
    header=['name','standard', 'date_of_addmition','paid','mark']
    table=tabulate([data4],headers=header,tablefmt='grid')
    f=open('myfile1.txt','a')
    f.write(table)
    f.close()
    return table
            


#to check the fees due 
def due_check(fees):
    global paid,due
    data={}
    data={'name':[name_s],'standard':[standard], 'date_of_addmition':[date_of_addmition],'paid':[paid]}
    due = fees - paid
    if due == 0:
        print('No due')
    else:
        print(f'Due: {due}')

    data5=[name_s,standard,date_of_addmition,paid,due]
    header=['name','standard', 'date_of_addmition','paid','due']
    table=tabulate([data5],headers=header,tablefmt='grid')
    f=open('myfile1.txt','a')
    f.write(table)
    f.close()
    return table

#to print all detail
def detail():
    global name_s,standard,date_of_addmition,due
    data={}
    data={'name':[name_s],'standard':[standard], 'date_of_addmition':[date_of_addmition],'due':[due],'marks':[mark]}
    data6=[name_s,standard,date_of_addmition,due,mark]
    header=['name','standard', 'date_of_addmition','due','mark']
    table=tabulate([data6],headers=header,tablefmt='grid')
    f=open('myfile1.txt','a')
    f.write(table)
    f.close()
    return table


try:
    with open('myfile1.txt', 'r') as f:
        existing_data = f.read()
        if existing_data.strip():
            print("Existing record found:")
            print(existing_data)
except FileNotFoundError:
    existing_data = None

# Only ask for student input if no record exists
if not existing_data:
    name_s = input('Enter the name of the student: ')
    standard = input('Enter the class: ')
    date_of_addmition = input('Enter the date of admission: ')
    paid = int(input('Enter the fees paid: '))
    print(create_record(name_s, standard, date_of_addmition, paid))
        
while True:
    print('1.TO ENTER NEW RECORD')  
    print('2.TO CHANGE THE NAME')  
    print('3.TO CHANGE THE STANDERED') 
    print('4.TO ENTER THE MARKS')  
    print('5.TO CHECK THE FEES DUE') 
    print('6.TO DISPLAY ALL THE DETAILS')
    print('7. TO EXIT')
    choice=int(input('Enter the choice: '))
    if choice==1:
        name_s=input('enter the name of the student: ')
        standard=input('enter the class: ')
        date_of_addmition=input('enter the date of addmition: ')
        paid=int(input('enter the fess paid: '))
        print(create_record(name_s,standard,date_of_addmition,paid)) 
        
    elif choice==2:
        new_name=input('enter new name of the student: ')
        print(name_change(new_name))
    
        
    elif choice==3:
        name_s=input("Enter the name of the student whose standard you want you change: ")
        new_standard=input('enter the standard: ')
        print(standard_change(new_standard))
        

    elif choice==4:
        mark=int(input('enter the marks: '))
        total_marks=int(input('enter the total weightage: '))
        name_s=input('enter the name of student: ')
        print(marks(mark,total_marks,name_s))

    elif choice==5:
        fees=int(input('enter the fees of the course'))
        print(due_check(fees))

    elif choice==6:
       print(detail())

    elif choice==7:
        break
print('PROGRAM ENDED')

    


        





    

    

