import csv
import sys

print("Гpyna 4")
filename= "/Users/kirillpetruska/Documents/python/students4.txt" 
text_file = open("/Users/kirillpetruska/Documents/python/students4.txt", "r")
reader=csv.reader(text_file, delimiter="\t")
for str in reader:
    print(str)
text_file.close()


print("Гpyna 5")
filename= "/Users/kirillpetruska/Documents/students5.txt" 
text_file = open("/Users/kirillpetruska/Documents/python/students5.txt", "r")
reader=csv.reader(text_file, delimiter="\t")
for str in reader:
    print (str) 
text_file.close()


print("Група 6")
filename= "/Users/kirillpetruska/Documents/python/students6.txt" 
text_file = open("/Users/kirillpetruska/Documents/python/students6.txt", "r")
reader=csv.reader(text_file, delimiter="\t")
for str in reader: 
    print(str)
text_file.close()
