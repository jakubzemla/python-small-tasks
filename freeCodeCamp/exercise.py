
# #_______PAY ALGO_______#
# def computepay(hours, rate):
#     if hours > 40:
#         regular_pay = 40.0 * rate
#         overtime_pay = (hours - 40.0) * (rate * 1.5)
#         to_pay = regular_pay + overtime_pay
#     else:
#         to_pay = hours * rate
#     return "{:.2f}".format(to_pay)

# string_hours = input("Enter Hours: ")
# string_rate = input("Enter Rate: ")

# try:
#     float_hours = float(string_hours)
#     float_rate = float(string_rate)
# except:
#     print("Error, please enter numeric input")
#     quit()


# print(f"Pay {computepay(float_hours, float_rate)}€")





#________LOOP EXERCISE_______#
# user_inputs = []
# sum = 0
# count = 0
# average = 0

# while True:
#     inp = input("Enter the number: ")
#     if inp == "done":
#         for num in user_inputs:
#             sum += num
#             count += 1
#         average = sum / count
#         print(sum, count, average)
#         break
#     try:
#         inp_float = float(inp)
#     except:
#         print("Invalid input")
#     user_inputs.append(inp_float)






#________OPEN & READ FILE________#
# fhand = open("mbox-short.txt")
# for line in fhand:
#     line = line.rstrip()
#     words = line.split()
#     # guardian
#     if len(words) < 3 or words[0] != "From":
#         continue
#     print(words[2])





#_______BIGGEST COUNT OF WORD IN FILE________#
# counts = dict()
# file_name = input("Enter the file name: ")
# if len(file_name) < 1: file_name = "clown.txt"
# file_handler = open(file_name)

# for line in file_handler:
#     line = line.rstrip()
#     line_words = line.split()
#     for word in line_words:
#         counts[word] = counts.get(word, 0) + 1

# max_count = 0
# max_word = None

# for key, value in counts.items():
#     if value > max_count:
#         max_count = value
#         max_word = key

# print(max_word + ":", max_count)





#________THE 5 MOST COMMON WORDS IN FILE_______#
# counts = dict()
# file_name = input("Enter the file name: ")
# if len(file_name) < 1: file_name = "clown.txt"
# file_handler = open(file_name)

# for line in file_handler:
#     line.rstrip()
#     line_words = line.split()
#     for word in line_words:
#         counts[word] = counts.get(word, 0) + 1

# common_words = sorted([(v,k) for k,v in counts.items()], reverse=True)
# print(common_words[:5])


# def computepay(hours, rate):
#     super_rate = rate * 1.5
#     if hours <= 40:
#         return hours * rate
#     else:
#         normal_pay = 40 * rate
#         extra_pay = (hours - 40) * super_rate
#         return normal_pay + extra_pay

# print(computepay(float(input("Enter the hours: ")), float(input("Enter the rate: "))))





#________INTEGERS INPUTS AND MAX MIN VALUE________#
# largest = 0
# smallest = None
# numbers = []
# while True:
#     num = input("Enter the integer number: ")     
#     if num == "done":
#         break
#     try:
#         num = int(num)
#     except ValueError:
#         num = "Invalid input"
#         print(num)
#     numbers.append(num)
#     smallest = numbers[0]

# for number in numbers:
#     if type(number) != int: continue
#     if number > largest:
#         largest = number
#     elif number < smallest:
#         smallest = number
    
# print(f"Maximum is {largest}")
# print(f"Minimum is {smallest}")





#________FIND FLOAT IN STRING________#
# text = "X-DSPAM-Confidence:    0.8475"
# first_num = None
# for letter in text:
#     try:
#         int(letter)
#         first_num = letter
#         break
#     except ValueError:
#         pass

# first_index = text.find(str(first_num))
# print(float(text[23:]))





#________FIND ALL FLOATS AND CALCULATE AVERAGE________#
# floats_list = []
# file_name = input("Enter the file name: ")
# file_handler = open(file_name)
# for line in file_handler:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     first_num = None
#     for letter in line:
#         try:
#             int(letter)
#             first_num = letter
#             break
#         except ValueError:
#             pass
#     first_index = line.find(str(first_num))
#     floats_list.append(float(line[first_index:]))

# total = 0
# for fl in floats_list:
#     total += fl

# print(f"Average spam confidence: {total/len(floats_list)}")





#________FIND SENDER WITH MAX MESSAGES________#
# file = input("Enter file: ")
# if len(file) < 1:
#     file = "mbox-short.txt"
# file_handler = open(file)

# senders_dict = {}

# for line in file_handler:
#     if line.startswith("From"):
#         #line = line.rstrip()
#         line_words = line.split(" ")
#         senders_dict[line_words[1]] = senders_dict.get(line_words[1], 0) + 1

# max_num = 0
# max_sender = ""
# for k, v in senders_dict.items():
#     if v > max_num:
#         max_num = v
#         max_sender = k
    

# print(max_sender, max_num)




#________LIST OF MESSAGES HOURS________#
# file_name = input("Enter file name: ")
# if len(file_name) < 1:
#     file_name = "mbox-short.txt"
# file_handler = open(file_name)
# cache = {}

# for line in file_handler:
#     if line.startswith("From:"): continue
#     elif line.startswith("From"):
#         line = line.rstrip()
#         last_index = line.find(":")
#         hour = line[last_index-2:last_index]
#         cache[hour] = cache.get(hour, 0) + 1
# hours_list = sorted([(hour, count) for hour, count in cache.items()])

# for tupl in hours_list:
#     print(tupl[0], tupl[1])





#________REGEX SUM OF INTEGERS IN TXT FILE________#
# import re

# list_numbers = []
# input_file = input("Enter the file name: ")
# with open(input_file, "r") as file:
#     for line in file:
#         line = line.rstrip()
#         matches = re.findall("[0-9]+", line)
#         if len(matches) < 1: continue
#         for num in matches:
#             list_numbers.append(int(num))
# print(sum(list_numbers))




#_______WRITE a WEB BROWSER - SOCKET_______#
# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
# mysock.close()





#________WRITE A WEB BROWSER - URLLIB________#
# import urllib.request, urllib.parse, urllib.error

# file_handler = urllib.request.urlopen("https://www.codexcoder.com/demos/templatemonster/anftyland-demo/cutemonster/index.html")
# for line in file_handler:
#     print(line.decode().strip())





#________WEB SCRAPPING WITH PYTHON________#
# http://www.dr-chuck.com/page1.htm

# import urllib.request, urllib.parse, urllib.error

# import soupsieve
# from bs4 import BeautifulSoup

# url = input("Enter url: ")
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')

# #retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get("href", None))





#________WEB BROWSER SOCKET TASK________#
# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(("data.pr4e.org", 80))
# command = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
# mysock.send(command)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(), end="")

# mysock.close()





#________SCRAPING NUMBERS FROM HTML USING BEAUTIFULSOUP________#
# import urllib.request, urllib.error, urllib.parse
# import re

# from bs4 import BeautifulSoup

# web_handle = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1555230.html")
# soup = BeautifulSoup(web_handle, "html.parser")

# numbers = list()
# tags = soup("span")
# for tag in tags:
#     tag = str(tag)
#     tag_nums = re.findall("[0-9]+", tag)
#     for num in tag_nums:
#         numbers.append(int(num))

# print(sum(numbers))





#________FOLLOWING LINKS IN PYTHON________#
# import urllib.request, urllib.parse, urllib.error
# import re

# from bs4 import BeautifulSoup

# current_url = "http://py4e-data.dr-chuck.net/known_by_Silas.html"
# name_from_url = re.findall("by_(.+).html$", current_url)
# name = name_from_url[0]
# if name == "Fikret":
#     index = 2
# else:
#     index = 17

# for url in range(7):
#     web_handler = urllib.request.urlopen(current_url)
#     soup = BeautifulSoup(web_handler, "html.parser")
#     anchors = soup("a")
#     names = [link.contents[0] for link in anchors]
#     links = [link.get("href", None) for link in anchors]
#     name += f" {names[17]}"
#     current_url = links[17]

# print(name)






#________EXTRACTING DATA FROM XML________#
# import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET

# web_handler = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1555232.xml")
# data = web_handler.read()
# tree = ET.fromstring(data)
# comment_list = tree.findall("comments/comment/count")
# comment_nums = sum([int(comm.text) for comm in comment_list])
# print(comment_nums)





#_________EXTRACTING DATA FROM JSON________#
# import json
# import urllib.request

# url_handler = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1555233.json")
# get_data = url_handler.read().decode()
# data = json.loads(get_data)
# comments = data["comments"]
# counts = [int(comment["count"]) for comment in comments]
# print(sum(counts))