import os
import shutil

rainbow_class = [
    "Yumi",
    "Sophia",
    "Miya",
    "Mia",
    "Yomi",
    "Aubrey",
    "Joey",
    "William",
    "Yoyo",
    "Eason",
    "Leo",
    "Yanike"
        ]

red_class = [
    "Ultraman",
    "Mason",
    "Toby",
    "May",
    "Ryan",
    "Phil",
    "Simon",
    "Allen",
    "Andy",
    "Sunny",
    "Yoyo",
    "Davey",
    "Amos",
    "Eric"
        ]

class_names = ["Red Class", "Rainbow Class"]

def make_directories():
    for c_index, c in enumerate(class_names):
        directory = class_names[c_index]
        if not os.path.exists(directory):
            print("File not found")
            print(f"Adding directory {directory}")
            os.mkdir(directory)
            print(f"Copy test papers")
        else:
            print("File Already Exists")


## Copy file and rename
def create_student_papers(class_name, student_list):
    for student in student_list:
        shutil.copy("paper.pdf", f"{class_name}/{student}.pdf")

# Make Class Directoies
make_directories()

# Copy and rename papers, sort into each class.
create_student_papers("Red Class", red_class)
create_student_papers("Rainbow Class", rainbow_class)
