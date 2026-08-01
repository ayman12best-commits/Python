# get rid of duplicates

student = {
    "id1" : {
        "name" : "sara",
        "grade": "XI",
        "subject" : ['English','Maths','Science']
    },
    "id2" : {
        "name" : "James",
        "grade": "XI",
        "subject" : ['Accounts','Maths','Science']
    },
    "id3" : {
        "name" : "sara",
        "grade": "XI",
        "subject" : ['English','Maths','Science']
    },
    "id4" : {
            "name" : "Christo",
            "grade": "XI",
            "subject" : ['CS','Maths','Science']
        }
}

unique = {}

for key,value in student.items():
    if value not in unique.values():
        unique[key] = value

print("Without duplicates")
print(unique)