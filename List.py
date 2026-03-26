#Working with Lists
#List function to add elements==> append(), insert()
#List function to remove elements ====> remove(), pop()
#Other List functions==> sort(), reverse()
print("========")
print("\nHello, this program lets you store and display students in your class\n")
print("========")

num_of_students = int(input("Hello, please enter the number of students in your Class: \n"))

#create empty list
studentList = []

for y in range(0, num_of_students):
    StudentDetails = input("Enter student detail: ")
    studentList.append(StudentDetails)

    


for x in studentList:
    print(x)