# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)

# student_heights = [180, 124, 165, 173, 189, 169, 146]
# sum_height = 0
# for student_height in student_heights:
#     sum_height += student_height

# average_height = float(round(sum_height / len(student_heights), 1))
# print(average_height)

# student_scores = [78, 65, 89, 606, 55, 91, 102, 89]
# highest_score = 0
# for student_score in student_scores:
#     if highest_score <= student_score:
#         highest_score = student_score
    
# print(highest_score)

total = 0
for number in range(1, 101):
    if number%2 == 0:
        total+=number
    else:
        print(f"Нечетные: {number}")
print(total)


