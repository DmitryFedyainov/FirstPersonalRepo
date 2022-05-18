# course = 'Python for "beginners"'
# print(course)
# print (course[0])
# print (course[-2])
# print (course[0:3])
# print (course[1:])
# print (course[:5])
# print (course[:])

# course = 'Jennifer'
# print (course[1:-1])

course = "Python for 'beginners'"
# print (course.upper())
# print (course.lower())
# print (course.find('P'))
# print (course.find('o'))
# print (course.find('0'))
# print (course.find('beginners'))
# print (course.replace('beginners', 'absolute beginners'))
# print('Python' in course)
# print('python' in course)
# print(len(course))

# course = '''
# Hi John,
#
# This is our first e-mail to you.
#
# Thank you,
# Support team
# '''
# print(course)                             # multiline string

# is_cold = False                           #if statements
# is_hot = False
# if is_cold:
#     print("Wear warm clothes, \n"
#           "because it's cold.")
# elif is_hot:
#     print("Drink planty of water, \n"
#           "it's hot outside.")
# else:
#     print("It's lovely day!")
# print("Enjoy your day!")

# price = 1000000
# has_good_credit = True
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}")

# has_high_income = True                    #logical operators
# has_good_credit = True
# if has_high_income and has_good_credit:
#     print("Eligible for loan")

# has_high_income = True
# has_good_credit = False
# if has_high_income or has_good_credit:
#     print("Eligible for loan")

# has_high_income = True
# has_criminal_record = False
# if has_high_income and not has_criminal_record:
#     print("Eligible for loan")

# name = input("Enter your Name: ")           #Comparison operators
# if len(name) < 3:
#     print("Name must be at least 3 characters.")
# elif len(name) > 10:
#     print("Name can be maximum 10 chracters.")
# else:
#     print("Good name.")

# weight = input("Enter your weight: ")
# measure = input("(L)bs or (K)g: ")
# if measure.upper() == "L":                    # .upper() позволяет пользователю указывать как lowercase, так и uppercase
#     print(f'You are: {int(weight) * 0.45} kg.')
# elif measure.upper() == "K":
#     print(f'You are {int(weight) * 2.20} lbs.')
# else:
#     print("Choose the correct measure.")

# started = False
# while True:                                  #While statement
#     game = input('> ').lower()
#     if game == 'help':
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to exit
# """)
#     elif game == 'start':
#         if started:
#             print("Cars is already started!")
#         else:
#             started = True
#             print('Car started. Ready to go!')
#     elif game == 'stop':
#         if not started:
#             print("Cars is already stopped!")
#         else:
#             started = False
#             print('Car stopped.')
#     elif game == 'quit':
#         print("The game canceled.")
#         break
#     else:
#         print("I don't understand.")


# for item in 'Python':                                 #For loops
#     print(item)

# for item in ['Mosh', 'John', 'Sarah']:
#     print(item)

# for item in [1, 2, 3, 4, 5, 6, 7]:
#     print(item)

# for item in range (100):
#     print(item)

# for item in range (10, 71, 10):
#     print(item)

# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")                #In Python source code, an f-string is a literal string, prefixed with ‘f’,
                                        # which contains expressions inside braces.
                                        #The expressions are replaced with their values.

# names = ['John', 'Mike', 'Mosh', 'Sarah', 'Mary']                 #Lisls
# print(names)
# print(names[0])
# print(names[-1])
# print(names[2:])
# print(names[2:3])
# print(names[:2])
# names[0] = 'Todd'
# print(names)

# numbers = [3, 6, 9, 12, 301, 25]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

numbers2 = [5, 2, 5, 6, 7, 5, 8]                        #list functions
#numbers2.append(20)               #adding 20 in the end of the list
#numbers2.insert(3, 30)            #adding 30 in the middle of the list
#numbers2.insert(0, 30)            #adding 30 in the begging ot the list
#numbers2.remove(6)                #removing from the list
#numbers2.clear()                  #clearing whole the list
#numbers2.pop()                    #removing the last from the list
#print(numbers2.index(5))          #showing index item in the list
#print(50 in numbers2)             #return boolean value in case of 50 is absent in the list
#print(numbers2.count(5))          #count items in the list
#numbers2.sort()                   #sorting items in the list in ascending order
#numbers2.reverse()                #sorting items in the list in descending order
#numbers3 = numbers2.copy()        #copy list to another variable
#print(numbers3)


