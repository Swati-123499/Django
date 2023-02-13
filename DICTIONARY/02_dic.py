

student = [
    {
        "name": "max",
        "age": 21,
        "university": "abc university",
        "grade": {
            "10th": 90,
            "12th": 80,
            "be": 85
        }
    },
    {
        "name": "lucy",
        "age": 21,
        "university": "abc university",
        "grade": {
            "10th": 92,
            "12th": 83,
            "be": 85
        }
    }
]


for i in range(len(student)):
    for j in student[i].keys():
        print(j),

    print(i, student[i])
