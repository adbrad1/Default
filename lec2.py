# Print Header Information
print("The Test Scores and Final Grade Program Repeating")
print()
print("Enter 3 Test scores")
print("====")

userValue="Y"

while(userValue=="Y"):
    # Get User Test Scores
    test1=int(input("Enter test score:  "))
    test2=int(input("Enter test score:  "))
    test3=int(input("Enter test score:  "))
    print("====")

    # Calculate Sum
    sum=test1+test2+test3
    avg=int(sum/3)

    # Print Results
    print("Total Score:  "+ str(sum))
    print("Average Score:  "+ str(avg))
    print()

    # Print Grade
    if(avg >=90) :
        grade="A"
    elif(avg>=80):
        grade="B"
    elif(avg>=70):
        grade="C"
    elif(avg>=60):
        grade="D"
    elif(avg>=0):
        grade="F"
    else:
        grade="?"
        
    print("The grade is " + grade + ".")

    if(grade!="F" and grade!="?"):
        print("You passed!")

    print()
    print()

    userValue=input("Would you like to continue? (y=yes n=no):  ")
    userValue=userValue.upper()
print()
print("Bye")

