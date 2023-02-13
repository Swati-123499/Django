
"""
student = {
    "name": "max",
    "age": 21,
    "university": "abc university",
    "grade": {
        "10th": 90,
        "12th": 80,
        "be": 85
    }
}
"""


student = {
    1: {
        "name": "max",
        "age": 21,
        "university": "abc university",
        "grade": {
            "10th": 90,
            "12th": 80,
            "be": 85
        }
    },
    2: {
        "name": "lucy",
        "age": 21,
        "university": "abc university",
        "grade": {
            "10th": 92,
            "12th": 83,
            "be": 85
        }
    }
}

for i in student.keys():
    #print(i, student[i].keys())
    for j in student[i].keys():
        print(j, student[i][j])
    print()


# print(student[1]["name"])
"""
grade = student["grade"]
print(grade["be"])
print(student["grade"]["be"])
print(student.keys())


print(student["name"])


for i in student.keys():
    print(i, student[i])
"""
