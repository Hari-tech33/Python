py_stud = {"afi", "ajay", "lokan" }

data_stud = {"afi", "ehan", "judy"}

py_stud.add("shantha")

data_stud.remove("ehan")

print(py_stud & data_stud)

print(py_stud - data_stud)

print(py_stud | data_stud)

course_new = {
  "python": len(py_stud),
  "data_science": len(data_stud)
}
for course, count in course_new.items():
    print(f"course: {course}, student: {count}" )

growth = {course: count * 2 for course, count in course_new.items()}

print("expected growth:", growth)

new_dict = {course: str(count) + " fullstack" for course, count in course_new.items()}
print(new_dict)
