import csv
from pathlib import Path


# Defining first function:
heading = ['Name','Age','Phone','Track']
def save_participant(path, participant_dict):
    path = Path(path)
    file_exists = path.exists()

    with open(path,"a",newline="",encoding="utf-8") as f:
        writer = csv.DictWriter(f,fieldnames=heading)
        # writer.writerow(participant_dict)

        if not file_exists:
            writer.writeheader()
        else:
          writer.writerow(participant_dict)

# Defining second function:
def load_participants(path):
    path = Path(path)

    if not path.exists():
        return {}

    with open(path,"r", newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        # for row in reader:
        #     print(f"{row}")

    
        for row_number, row in enumerate(reader):
           if row_number == 0:  # Header row
            print(f"Headers: {' | '.join(row)}")
            print("-" * 40)
           else:  # Data rows
            print(f"{row}")
  



