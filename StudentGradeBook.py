# Student Grade book

Student_Grade_Book = { "Ayman" : 98,
                       "Ronaldo" : 68,
                        "Neymar" : 79,
                        "Messi" : 99,
                        "Thawban" : 98 }

sum = 0
for key,value in Student_Grade_Book.items():
    sum = sum + value
print("The total marks are : ", sum)
avg = sum / len(Student_Grade_Book)
print("The average marks are : ", avg)
print(min(Student_Grade_Book.values()))
print(max(Student_Grade_Book.values()))
print(Student_Grade_Book.get("Ayman"))
Name = input("Enter the Name to search for the marks : ")
print(Student_Grade_Book.get(Name))