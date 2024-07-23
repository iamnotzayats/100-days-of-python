# String
# Integer
# Float
# Boolean

# Выводит только n-ный указанный символ
# print("Hello"[2])
# print(123_456_789)

# Выводит длину тип длины введенной строки
# type_number = len(input("Enter something: "))
# new_type_number = float(type_number)
# print("NEW "+new_type_number)
# print(type(type_number))

# type_number = float(123) 
# print(type_number+76.3)

# home work 1
# number = input("Enter a random number: ")
# result = int(number[0]) + int(number[1])
# print(result)

# 2 ** 3 = 8 ( пример вывода 2 в степени 3 = 8)

# home work 2
# height = float(input("HEIGHT: "))
# weight = int(input("WEIGHT: "))

# bmi_result = weight/height ** 2
# # or bmi_result = (weight/(height*height))
# print(float(bmi_result))

# # round - округление
# print(round(8/3, 2))
# # // - деление без остатка
# print(8 // 3)

# score = 0
# score += 1
# # f-stirings
# print(f"TEXT {score} TEXT2")

# home work 3
total_price = float(input("Общая сумма: "))
tip = int(input("Процент чаевых(сколько хотите дать? 10%, 15%, 20%?): "))
result = float((total_price * tip)/100)
print(f"Чаевые составили: {round(result, 2)} ")
