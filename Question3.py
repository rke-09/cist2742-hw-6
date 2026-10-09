# Question 3 

def classify_age():

    age = int(input("Enter your age: "))

    if age < 0:
        print("Invalid age")
    elif age <= 12:
        print("Child")
    elif age <= 19:
        print("Teenager")
    elif age <= 65:
        print("Adult")
    else: 
        print("Senior")

    if age > 100:
        print("Congratulations for appearing on the Smucker's jar!")

classify_age()
