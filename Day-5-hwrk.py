frontend = {"joby", "nirmal", "loka", "safa"}
backend = {"joby", "nevin", "surya", "sena"}

backend.add("rahul")

frontend.remove("loka")

print(frontend & backend)

print(frontend - backend)

print(frontend | backend)

course = {
    "frontend": len(frontend),
    "backend": len(backend)
}
print(course)
for course, count in course.items():
    print(f"course: {course}, students: {count}")

