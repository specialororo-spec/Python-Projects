print("Enter name:")
name = input()
print(f"Hello {name}")

print("Enter your jamb_score:")
jamb_score =int(input())

print("Enter your age:")
age = int(input())

print("Have you paid tuition? (yes/no):")
tuition_payment =input().strip().lower()=="yes"


if jamb_score >= 190:
    print("Passed")
else:
    print("Sorry you failed")

if age >= 16:
    print('You are old enough')
else:
    print("You are too young")

if tuition_payment is True:
    print("Tuition is paid")
else:
    print("Tuition pending")

if jamb_score >=190 and age>=16 and tuition_payment:
    print("You have been accepted")
else:
    print("You have not been accepted")

