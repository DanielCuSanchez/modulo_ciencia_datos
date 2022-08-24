from multiprocessing.forkserver import ensure_running


students = ["Andrea", "Zaira", "Yesenia", "Oscar", "Damian", "Mariela"]

# students.sort()
students.sort(key = str.capitalize, reverse=True)

print(students)