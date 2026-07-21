import os
os.system("cls")

math = float(input("Math score: "))
social = float(input("Social score: "))
code = float(input("Code score: "))

def calculate_average_score(math, social, code):
    average = (math + social + code) / 3
    print(average)

    if average >= 90:
        print("Grade A")
    elif average >= 80:
        print("Grade B")
    elif average >= 70:
        print("Grade C")
    elif average >= 60:
        print("Grade D")
    elif average >= 50:
        print("Grade E")
    else:
        print("You Failed")

calculate_average_score(math, social, code)
