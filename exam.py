totaldays=int(input("Enter total no.of days:"))
present=int(input("Enter no.of days present"))
attendance = present/totaldays*100
if attendance>= 75:
    print("You are eligible to write the exam")
else:
    print("You are not eligible to write the exam")
