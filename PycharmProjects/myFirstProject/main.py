
# character_name = "Tom"
# character_age = 50
# print("Hi, my name is " + character_name)
# print("I'm " + str(character_age) + " years old")

#print("Giraffe\nAcademy")

# my_num = 5
# print(my_num)

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! " + "You are " + age)

# num1 = input("Enter a first number: ")
# num2 = input("Enter a second number: ")
# result = float(num1) + float(num2)
# print(result)

# friends = ["Mike", "Karen", "Jim", "Bim", "Todd", "Shake"]
# friends[0] = "Kate"
# print(friends[0])

# lucky_numbers = [4, 8, 15, 23, 42]
# friends = ["Mike", "Karen", "Jim", "Bim", "Todd", "Shake"]
# friends.extend(lucky_numbers)
# print(friends)

# lucky_numbers = [4, 8, 15, 23, 42]
# friends = ["Mike", "Karen", "Jim", "Bim", "Todd", "Shake"]
# friends.append("Frank")
# print(friends)

# lucky_numbers = [4, 8, 15, 23, 42]
# friends = ["Mike", "Karen", "Jim", "Bim", "Todd", "Shake"]
# friends.insert(1, "Kelly")
# print(friends)

# lucky_numbers = [4, 8, 15, 23, 42]
# friends = ["Mike", "Karen", "Jim", "Bim", "Todd", "Shake"]
# friends.remove("Jim")
# print(friends)

# lucky_numbers = [4, 8, 15, 23, 42]
# friends = ["Mike", "Karen", "Jim", "Bim", "Todd", "Shake"]
# friends.clear()
# print(friends)

# lucky_numbers = [4, 8, 15, 23, 42]
# friends = ["Mike", "Karen", "Jim", "Bim", "Todd", "Shake"]
# friends.pop()
# print(friends)

# lucky_numbers = [4, 8, 15, 23, 42]
# friends = ["Mike", "Karen", "Jim", "Bim", "Todd", "Shake"]
# print(friends.index("Jim"))

# lucky_numbers = [4, 8, 15, 23, 42]
# friends = ["Mike", "Karen", "Jim", "Jim", "Jim", "Bim", "Todd", "Shake"]
# print(friends.count("Jim"))

# lucky_numbers = [34, 56, 78, 4, 8, 15, 23, 42]
# lucky_numbers.sort()
# print(lucky_numbers)

# lucky_numbers = [34, 56, 78, 4, 8, 15, 23, 42]
# lucky_numbers.reverse()
# print(lucky_numbers)

# lucky_numbers = [34, 56, 78, 4, 8, 15, 23, 42]
# lucky_numbers2 = lucky_numbers.copy()
# print(lucky_numbers2)

# def say_hi():
#     print("Hello user")
# say_hi()

# def say_hi():
#     print("Hello user")
# print("Запупка")
# say_hi()
# print("Кто запупка?")

# def say_hi(name):
#     print("Hello " + name + "!")
# say_hi("Mike")

# def say_hi(name, age):
#     print("Hello " + name + "! You are " + str(age) + ".")
# say_hi("Mike", 78)

# def pull(num):
#     return (num+num)*12
# print(pull(5))

# def pull(num):
#     return (num+num)*12
# result = pull(5)
# print(result)

# is_male = False
# if is_male:
#     print("You are a male")
# else:
#     print("You are not a male")

# is_male = False
# is_tall = False
# if is_male or is_tall:
#         print("You are a male or tall or both")
# else:
#         print("You neither male nor tall")

# is_male = True
# is_tall = True
# if is_male and is_tall:
#         print("You are a male and tall")
# else:
#         print("You neither male nor tall")

# is_male = True
# is_tall = False
# if is_male and is_tall:
#     print("You are a male and tall")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are not a male but tall")
# else:
#     print("You neither male nor tall")

# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
# print(max_num(1,2,3))

#Building a better Calculator
# num1 = float(input("Enter a first number: "))
# op = input("Enter an operator: ")
# num2 = float(input("Enter a second number: "))
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")

#Dictionaries
# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar":"March"
# }
# print(monthConversions["Jan"])
# print(monthConversions.get("luv")) #чтобы не получить ошибку, если значения нет в словаре

#while loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#
# print("Done whit loop")

#guessing game
# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("Out of guesses. You lose!")
# else:
#     print("You win!")

#For Loop
# for letter in "Giraffe Academy":
#     print(letter)

# friends = ["Jim", "Karen", "Kevin"]
# for friends in friends:
#     print(friends)

# friends = ["Jim", "Karen", "Kevin"]
# for index in range(len(friends)):
#     print(friends[index])

#Try
#Except

# try:
#     #answer = 10/0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("Invalid input")