num_of_courses = int(input("How many courses will you enter grades for? "))

total = 0
for i in range(num_of_courses):
    grade = float(input(f"Enter grade for course {i+1}: "))
    total += grade

average = total / num_of_courses
print(f"Your GPA: {average:.2f}")

if average >= 50:
    print("Congratulations, you passed! 🎉")
else:
    print("Sorry, you failed. 😞")
