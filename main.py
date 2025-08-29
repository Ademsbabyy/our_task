
from file_ops import save_participant,load_participants
from pathlib import Path
import csv
csv_file = 'participants.csv'
workspace = Path("participant_pkg")

print("\tCONTACT SAVER")
print("You are welcome to the Publica tech workshop\nPlease do well to fill in correct details\nThank You!")

participant_dict = {}
while True:
    try: 
        name = input("What is your name?")
        if not name.isalpha():
            raise ValueError("Invalid input")
        if name == "":
         print("Name cannot be empty")
         continue
        else:
         age = input("How Old are you?")
         try:
              age = int(age)
         except:
              print("Your age must be a number!\nplease try again")
              age = int(input("Enter your age: "))
              continue
         else:
          phone = input("Enter your phone number: ")
         if not phone.isdigit() :
             print("The phone number must contain only numbers")
         elif len(phone) != 11:
            print("The phone number must be eleven")
         elif not phone.isdigit() and len(phone) != 11:
            print("Please enter the right number!")
            continue
         else:
           track = input("Enter your track: ")
           if track == "":
            print("Track cannot be empty!")
           else:
            print("Valid track")
        break   
    except ValueError as e:
        print("Error:", e)

participant_dict = {name, age, phone, track}
# participant = { 
#    "name", "age", "phone", "track",  
#     name, age, phone,track
#     }

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



















#     # # Save the data to a JSON file
#     # csv_file = workspace / "contact.csv"
#     # with open(csv_file, "w", encoding="utf-8") as f:
#     #     file_ops.save_participant()  # indent=2 makes it pretty and readable

#     # print("Participant data saved to csv file!")

#     # # Now read it back
#     # with open(csv_file, "a", encoding="utf-8") as f:
#     #     file_ops.load_participants()
#     #     load_participants = csv.load(f)

#     # print("\nData read from csv:")
#     # print(f"name: {load_participants['name']}")
#     # print(f"Age: {load_participants['age']}")
#     # print(f"phone_number: {load_participants['phone_number']}")
#     # print(f"track: {load_participants['track']}")

# #  # calling file_ops.save_participant
# #     try: 
# #       file_ops.save_participant()
# #     except:
# #       print("I/O Error")
# #     break

# # print("\nContact saver summary")
# # file_ops.load_participants(f"")