import csv
from pathlib import Path
from file_ops import save_participant,load_participants



""" The file below was written to test the file opps"""


csv_file = 'participants.csv'

while True:
    name = input("Enter your name: ")
    if name =="":
        print("Name cannot be empty")
    else:
     phone = input("Enter your phone number: ")

     if not phone.isdigit() :
        print("The phone number must contain only numbers")
     elif len(phone) != 11:
        print("The phone number must be eleven")
     elif not phone.isdigit() and len(phone) != 11:
         print("Please enter the right number!")
     else:
        track = input("Enter your track: ")
        if track == "":
           print("Track cannot be empty!")
        else:
           age = input("Enter your age: ")
           try:
              age = int(age)
           except:
              print("Your age must be a number!,please try again")
              age = int(input("Enter your age: "))
              break
        break


participant =  {
   'Name' : name,
    'Age' : age,
    'Track' : track,
    'Phone' : phone

}



save_participant(csv_file,participant)
all_participants = load_participants(csv_file)

for i in all_participants:
   print(i)


try:
 for index, i in enumerate(all_participants):
   if index == 0:  # Header row
      print(f"Headers: {' | '.join(i)}")
      print("_" * 40)

   else:
      print(i)
except :
   print("Try again!")
