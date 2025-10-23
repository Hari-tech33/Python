attendance = [18, 20, 19, 15, 21]
full_days = 0

for x in attendance:
    if x >= 20 :
        print("Full")
        full_days += 1
    else:
        print("not full")

print(full_days)

total_attendance = sum(attendance)
print(total_attendance)
