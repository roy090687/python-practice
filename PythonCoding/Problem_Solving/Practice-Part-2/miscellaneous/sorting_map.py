def sort_pure_map():
    data = {
        "banana": 3,
        "apple": 5,
        "cherry": 2,
        "date": 4
    }

    sorted_map = sorted(data.items(), key=lambda e: e[1])
    print(sorted_map)
    for item, count in sorted_map:
        print(item, ":", count)

def sort_pure_map_manual():
    data = {
        "banana": 3,
        "apple": 5,
        "cherry": 2,
        "date": 4
    }
    data_list = list(data.items())
    n = len(data_list)
    for i in range(n):
        for j in range(i+1, n):
            if data_list[i][1] > data_list[j][1]:
                data_list[i], data_list[j] = data_list[j], data_list[i]

    print(data_list)
    for item, count in data_list:
        print(item, ":", count)

def sort_list_of_map():
    students = [
        {"name": "Snehasish", "score": 85},
        {"name": "Rahul", "score": 92},
        {"name": "Priya", "score": 78},
        {"name": "Anita", "score": 88}
    ]
    students_map = sorted(students, key=lambda e: e["score"])
    print(students_map)
    for student in students_map:
        print(student["name"], ":", student["score"])

def sort_list_of_map_manual():
    students = [
        {"name": "Snehasish", "score": 85},
        {"name": "Rahul", "score": 92},
        {"name": "Priya", "score": 78},
        {"name": "Anita", "score": 88}
    ]
    n = len(students)
    for i in range(n):
        for j in range(i + 1, n):
            score1 = students[i]["score"]
            score2 = students[j].get("score")
            if score1 > score2:
                students[i], students[j] = students[j], students[i]

    for student in students:
        print(student["name"], ":", student["score"])


# Calling
print("----------- 1st O/P -----------")
sort_pure_map()

print("----------- 2nd O/P -----------")
sort_pure_map_manual()

print("----------- 3rd O/P -----------")
sort_list_of_map()

print("----------- 4th O/P -----------")
sort_list_of_map_manual()
