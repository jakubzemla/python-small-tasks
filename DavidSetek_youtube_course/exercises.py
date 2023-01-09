# __________________HORSKÁ DRÁHA____________________________#
# print("Welcome to the roller-coaster")
# height = int(input("What's your height?\n"))
# bill = 0
# if height >= 87:
#     print("You can go on a roller-coaster.")
#     age = int(input("How old are you?\n"))
#     if age < 12: 
#         bill = 4
#         print(f"Ticket costs {bill}€.")
#     elif age < 18: 
#         bill = 5
#         print(f"Ticket costs {bill}€.")
#     elif age >= 40 and age <= 50:
#         bill = 0
#         print("Ticket is free.")
#     else: 
#         bill = 6
#         print(f"Ticket costs {bill}€.")

#     photo = input("Do you want to take a picture while driving? Type 'yes' or 'no'\n")
#     if photo == "yes":
#         bill += 2
#         print(f"Ticket with photo costs {bill}€")
# else: print("We are very sorry, but you cannot go on a roller-coaster.")





#___________________BMI____________________#
# height = float(input("What's your height in metres?\n"))
# weight = float(input("What's your weight in kilograms?\n"))
# bmi = weight / height**2
# print(f"Your BMI is {round(bmi, 1)}.")
# if bmi < 18.5:
#     print("You are underweight.")
# elif bmi <= 24.9:
#     print("You are normal.")
# elif bmi <= 29.9:
#     print("You are overweight.")
# else:
#     print(f"Your are obese.")





#_____________PRESTUPNÝ ROK______________#
# def is_gap_year(year:int):
#     return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False

# def get_days_in_month(month:int):
#     days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     return 29 if gap_year == True and month == 2 else days_in_month[month - 1]

# gap_year = is_gap_year(int(input("Enter the year: ")))
# days = get_days_in_month(int(input("Enter the month in number format: ")))
# print(f"The number of days in seleced month is {days}.")





#___________PIZZA_______________#
# print("Welcome to our order form.")
# price = 0
# size = input("What size of your pizza do you want? Type 'S' for small, 'M' for medium or 'L' for large pizza: ")
# pepperoni = input("Do you want add a pepperoni? Type 'yes' or 'no': ")
# extra_cheese = input("Do you want add extra cheese? Type 'yes' or 'no': ")

# if size == "S": price = 4
# elif size == "M": price = 5
# else: price = 6

# if pepperoni == "yes" and size == "S": price += 1
# elif pepperoni == "yes": price += 1.50

# if extra_cheese == "yes": price += 0.50

# print("Your pizza will cost", "{:.2f}".format(price) + "€")





#___________HARRY POTTER - GAME ____________#
# print("""
#  _                                       _   _            
# | |                                     | | | |           
# | |__   __ _ _ __ _ __ _   _ _ __   ___ | |_| |_ ___ _ __ 
# | '_ \ / _` | '__| '__| | | | '_ \ / _ \| __| __/ _ \ '__|
# | | | | (_| | |  | |  | |_| | |_) | (_) | |_| ||  __/ |   
# |_| |_|\__,_|_|  |_|   \__, | .__/ \___/ \__|\__\___|_|   
#                         __/ | |                           
#                        |___/|_|     


# """)
# print("Dear students, Welcome to Hogwarts!")
# print("Now you go to your rooms.")
# follow = input("Do you want to follow others and go to your room with your classmates? Type 'yes' or 'no': ").lower()
# if follow == "yes":
#     stay = input("You go up the self-propelled stairs with the others. You have come to the common room. Do you want to stay or go to your room? Type 'stay' or 'room': ").lower()
#     if stay == "stay":
#         print("You stay with others and taste magical sweets - THE END")
#     else:
#         print("A beautiful magical night - THE END")
# else:
#     choose = input("You disconnected from your classmates. Do you want to go left or right? Type 'left' or 'right': ").lower()
#     if choose == "left":
#         print("You hit a janitor Filch and he will escort you to your room - THE END")
#     else:
#         door = input("You see a courtyard door in front of you. Do you want to go out? Type 'yes' or 'no: ").lower()
#         if door == "yes":
#             print("It's cold outside and you'd better go back to your room - THE END")
#         else:
#             print("You stand alone in the hallway, bored. You'd better go back to your room - THE END")





#_______HÁDZANIE MINCE________#
# import random
# num = random.randint(0,1)
# result = "HEAD" if num == 0 else "EAGLE"
# print(result)





#________RICH PEOPLE IN RESTAURANT________#
# import random
# names = input("Write the names of your friends separated by comma:\n")
# list_names = names.split(", ")
# random_number = random.randint(0,  len(list_names) - 1)
# print(random_number)
# print(list_names[random_number], "will pay the bill today.")





#________OZNAČOVANIE POZÍCIÍ________#
# list1 = ["🐶", "🐶", "🐶"]
# list2 = ["🐶", "🐶", "🐶"]
# list3 = ["🐶", "🐶", "🐶"]
# common_list = [list1, list2, list3]
# position1 = int(input("Enter the first position from 0 to 2: "))
# position2 = int(input("Enter the second position from 0 to 2: "))
# common_list[position1][position2] = "❌"
# print(f"{list1}\n{list2}\n{list3}\n")





#________KAMEŇ, PAPIER, NOŽNICE_______#
# import random

# rock = '''
#     ROCK
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
 
# paper = '''
#     PAPER
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
 
# scissors = '''
#     SCISSORS
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# choices = [rock, paper, scissors]

# user_choice = choices[int(input("What's your choice? Type '0' for rock, '1' for paper or '2' for scissors: "))]
# ai_choice = choices[random.randint(0, 2)]
# print(f"You choosed:\n{user_choice}\n")
# print(f"PC choosed:\n{ai_choice}\n")

# if user_choice == ai_choice:
#     print("DRAW")
# elif (user_choice == rock and ai_choice == scissors) or (user_choice == paper and ai_choice == rock) or (user_choice == scissors and ai_choice == paper):
#     print("YOU WON")
# else:
#     print("YOU LOSE")





#________FOR A PRIEMERNÁ VÝŠKA________#
# heights = input("Zadajte rôzne výšky v cm:\n")
# arr_heights = heights.split(", ")
# sum = 0
# for height in arr_heights:
#     sum += float(height)
# print("{:.2f}".format(sum / len(arr_heights)) + "cm")


#_______FOR A MAX A MIN V LISTE_______#
# numbers_list = [50, 30, 12, 8, 1, 94]
# max = numbers_list[0]
# min = numbers_list[0]
# for num in numbers_list:
#     if num > max:
#         max = num
#     if num < min:
#         min = num
# print(f"Max: {max}\nMin: {min}")


#________FIZZ BUZZ GAME_______#
# for num in range(1, 31):
#     if num % 3 == 0 and num % 5 == 0: 
#         print("FizzBuzz ", end="")
#         print(num)
#     elif num % 3 == 0: 
#         print("Fizz ", end="")
#         print(num)
#     elif num % 5 == 0: 
#         print("Buzz ", end="")
#         print(num)
#     else: print(num)





#________GENERÁTOR NÁHODNÉHO HESLA_______#
# import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

# user_letters = int(input("How many letters do you want in your password? "))
# user_numbers = int(input("How many numbers do you want in your password? "))
# user_char = int(input("How many special characters do you want in your password? "))

# listed_password = []
# for letter in range(0, user_letters):
#     listed_password.append(random.choice(letters))
# for number in range(0, user_numbers):
#     listed_password.append(random.choice(numbers))
# for char in range(0, user_char):
#     listed_password.append(random.choice(special_char))

# random.shuffle(listed_password)
# password = ""
# for char in listed_password:
#     password += char
# print(password)





#_______HÁDACIA HRA - HARRY POTTER________#
# import random

# print("Vítajte v hádacej hre Harry Potter")

# characters = ["Harry", "Ron", "Hermiona", "Draco", "Crabbe", "Goyle", "Albos"]
# character = characters[random.randint(0, len(characters) - 1)]
# guess = ""
# guess_count = 5

# while character != guess:
#     if guess_count != 0:
#         guess = input("Uhádnite postavu z filmu Harry Potter: ")
#         guess_count -= 1
#         print(f"Počet zostávajúcich pokusov: {guess_count}")
#     else:
#         print(f"Počet pokusov je vyčerpaný. Hľadané slovo bolo '{character}'. Koniec hry")
#         break
#     if character == guess:
#         print(f"Uhádol si. Hľadané slovo bolo '{character}'. Gratulujeme!")





#_____WALL PAINT CALCULATOR________#
# import math
# def wall_paint_calculator(wall_width, wall_height, can_volume = 5):
#     area = wall_width * wall_height
#     result = math.ceil(area / can_volume)
#     return f"You are going to need a {result} cans"

# print(wall_paint_calculator(float(input("Enter the width of wall in meters: ")), float(input("Enter the height of wall in meters: "))))





#________PRVOČÍSLO________#
# def is_prime_number(number):
#     for num in range(2, number):
#         if number % num == 0: return "not a prime number"
#     return "PRIME NUMBER!!"

# print(is_prime_number(77))





#________CÉSAROVÁ ŠIFRA________#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def cipher(string, num, type):
#     result = ""
#     for letter in string:
#         if letter == " ":
#             result += letter
#             continue
#         index = alphabet.index(letter)
#         if type == "encode":
#             result += alphabet[index + num]
#         elif type == "decode":
#             result += alphabet[index - num]
#     return result

# word = input("Enter the message: ").lower()
# process = input("Type 'encode' to encrypt or type 'decode' to decrypt: ").lower()
# shift = int(input("Type the shift number: "))
# print(cipher(word, shift, process))





#________STUDENT'S RESULTS________#
# students_results = {
#     "Harry": 85,
#     "Ron": 71,
#     "Hermione": 98,
#     "Draco": 69
# }

# students_status = dict()
# for key, value in students_results.items():
#     if value > 90: students_status[key] = "excellent"
#     elif value > 80: students_status[key] = "great"
#     elif value > 70: students_status[key] = "good"
#     else: students_status[key] = "not pass"

# print(students_status)



#________NESTING DICTIONARIES AND LISTS________#
# travel_diary_dict = {
#     "Spain": {"Cities": ["Madrid", "Leon", "Valencia"], "Visits": 5},
#     "France": {"Cities": ["Paris", "Nice", "Rennes"], "Visits": 2}
# }

# travel_diary_list = [
#     {
#         "country": "Spain",
#         "cities": ["Madrid", "Leon", "Valencia"],
#         "visits": 5
#     },
#     {
#         "country": "France",
#         "cities": ["Paris", "Nice", "Rennes"],
#         "visits": 2
#     }
# ]

# def add_country(country: str, cities: list, visits: int):
#     travel_diary_list.append({
#         "country": country,
#         "cities": cities,
#         "visits": visits
#     })

# add_country("Czech Republic", ["Prague", "Brno", "Ostrava"], 3)
# print(travel_diary_list)





#________SILLENT AUCTION________#
# import os
# print("Welcome in the silent auction")
# offers = dict()
# def get_offer(name, value):
#     offers[name] = value
#     is_next_bidder = input("Is there another bidder? Type 'yes' or 'no': ")
#     if is_next_bidder == "yes":
#         get_offer(input("What's your name?: "), float(input("How much do you want to offer? ")))
#     else:
#         os.system("cls")
#         max_offer = 0
#         winner = 0
#         for bidder, offer in offers.items():
#             if offer > max_offer:
#                 max_offer = offer
#                 winner = bidder
#         print(f"Winner is {winner}, with his bid {max_offer}")
#         print(offers)


# get_offer(input("What's your name?: "), float(input("How much do you want to offer? ")))¨





#________CALCULATOR________#
# def get_calculate(num1, operation, num2):
#     if operation == "+": return num1 + num2
#     elif operation == "-": return num1 - num2
#     elif operation == "*": return num1 * num2
#     elif operation == "/": return num1 / num2
#     else: return "Error: You entered wrong mathematical operation"

# user_continue = True
# user_decide = ""
# result = 0

# while user_continue:
#     if user_decide != "yes":
#         num1 = input("Enter the first number: ")
#     else: num1 = result
#     print("""
#     +
#     -
#     *
#     /
#     """)
#     operation = input("Choose one from the operations above: ")
#     num2 = input("Enter the second number: ")
#     try:
#         num1 = float(num1)
#         num2 = float(num2)
#     except:
#         print("Only number value is allowed! Program ends")
#         exit()
#     result = get_calculate(num1, operation, num2)
#     print(f"{num1} {operation} {num2} = {result}")
#     user_decide = input("Would you like to continue on counting? Type 'yes' or 'no': ")
#     if user_decide != "yes": user_continue = False





#________GUESS THE NUMBER GAME________#
# import random
# import os
# print("Welcome. This is 'GUESS THE NUMBER' game. Try to defeat computer!\nThe computer will generate a secret number from 1 to 100 and you have to guess what number computer generated.")
# def init():
#     ai_number = random.randint(1, 100)
#     difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")
#     if difficulty == "easy": lives = 10
#     else: lives = 5
#     print(f"The game has begun. Lives left: {lives}")
#     guess_number(lives, ai_number)

# def guess_number(live, ai_num):
#     user_guess = int(input("Guess the number: "))
#     if user_guess > ai_num: 
#         print(f"Too high. Lives left: {live - 1}.")
#         sub_live(ai_num, live)
#     elif user_guess < ai_num: 
#         print(f"Too low. Lives left: {live - 1}.")
#         sub_live(ai_num, live)
#     else: 
#         print(f"YOU WON! The number was {ai_num}")
#         is_again()

# def sub_live(ai_num, live):
#     live -= 1
#     if live > 0: guess_number(live, ai_num)
#     else: 
#         print(f"YOU LOSE! The number was {ai_num}")
#         is_again()

# def is_again():
#     user_decide = input("Would you like to play again? Type 'yes' or 'no': ")
#     if user_decide == "yes":
#         os.system("cls")
#         init()
#     else:
#         os.system("cls")
#         exit()

# init()





#________DEBUGGING - ladění, hledání chyb________#
# def test_function():
#   for number in range(1, 10): #KUBO: range posledné číslo nezahŕňa! => range(1, 11)
#     if number == 10:
#       print("Vše je správně")
# test_function()
 
# Občas funguje a občas ne
# import random
# all_dice_numbers = ["1", "2", "3", "4", "5", "6"] 
# dice_number = random.randint(1, 6) #KUBO: ak vygeneruje č.6, bude index out of range! => random.randint(0, 5)
# print(all_dice_numbers[dice_number])
 
# Mysli jako počítač
# year = int(input("Jaký je váš rok narození?")) 
# if year > 1980 and year < 1994:
#   print("Jste millenial.")
# elif year > 1994: #KUBO: ak napíšeš 1994, nebude vedieť zaradiť.... treba k jednej podmienke pridať <= alebo >=
#   print("Jste generace Z.")
 
# # Oprav hned chyby
# age = input("Kolik je vám let?")
# if age > 18:
# print("Ve věku {age} můžete kupovat alkohol.") #KUBO: chýba odsadenie a označenie f stringu! Chýba premena dátového typu premenej age zo stringu na číslo 





#________THE HIGHER LOWER GAME________#
# data = [
#     {
#         'name': 'Instagram',
#         'follower_count': 501,
#         'description': 'Sociální platforma',
#         'country': 'USA'
#     },
#     {
#         'name': 'Facebook',
#         'follower_count': 4,
#         'description': 'Sociální platforma',
#         'country': 'USA'
#     },
#     {
#         'name': 'Cristiano Ronaldo',
#         'follower_count': 436,
#         'description': 'Fotbalový hráč',
#         'country': 'Portugal'
#     },
#     {
#         'name': 'Instagram',
#         'follower_count': 501,
#         'description': 'Sociální platforma',
#         'country': 'USA'
#     },
#     {
#         'name': 'Dwayne Johnson',
#         'follower_count': 161,
#         'description': 'Herec a wrestler',
#         'country': 'USA'
#     },
#     {
#         'name': 'Harry Potter film',
#         'follower_count': 8,
#         'description': 'Film',
#         'country': 'USA'
#     },
#     {
#         'name': 'Kim Kardashian',
#         'follower_count': 307,
#         'description': 'Podnikatelka',
#         'country': 'USA'
#     },
#     {
#         'name': 'Lionel Messi',
#         'follower_count': 324,
#         'description': 'Fotbalista',
#         'country': 'Argentina'
#     },
#     {
#         'name': 'Neymar',
#         'follower_count': 158,
#         'description': 'Fotbalista',
#         'country': 'Brazilie'
#     },
#     {
#         'name': 'Eminem',
#         'follower_count': 40,
#         'description': 'Hudebník',
#         'country': 'USA'
#     },
#     {
#         'name': 'Justin Bieber',
#         'follower_count': 193,
#         'description': 'Hudebník',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Emma Watson',
#         'follower_count': 111,
#         'description': 'Herečka',
#         'country': 'Francie'
#     }
# ]

# import random

# def init(A, B, score):
#     print(f"Porovnajte A: {data[A]['name']}, {data[A]['description']}, {data[A]['country']}")
#     print(f"Porovnajte B: {data[B]['name']}, {data[B]['description']}, {data[B]['country']}")
#     user_guess = input("Napíš možnosť 'A' alebo možnosť 'B': ").upper()
#     if user_guess == "A": user_index = A
#     elif user_guess == "B": user_index = B
#     else:
#         print(f"Nebolo možné vybrať možnosť {user_guess}. Program končí.")
#         exit()
#     get_compare(A, B, user_index, score)

# def get_compare(A, B, user_i, score):
#     if data[user_i]['follower_count'] == max([data[A]['follower_count'], data[B]['follower_count']]):
#         score += 1
#         print(f"Uhádol si. Tvoje aktuálne skóre je {score}.\n")
#         init(B, random.randint(0, len(data) - 1), score)
#     else: 
#         print(f"Nesprávny tip. Prehrávaš. Tvoje konečné skóre je {score}.\n")
#         exit()

# init(random.randint(0, len(data) - 1), random.randint(0, len(data) - 1), 0)