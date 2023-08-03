# This is a nested Condition program
# This programm will check are you eligable for admission or NoT


S_name = input("Student Name : ")

S_age = int(input("Please input your age : "))

if S_age>= 18:
    pass

    S_result = input("Please input your previous result : ")

    if S_result == "A+" or S_result == "A-" or S_result == "A":

        S_area = input("Are you Local student? (y/n) : ")
        if S_area == "y":

            print("Congratulation!")
            exit

        else:
            print("You are not eligibale to admission")
    else:

        print("Please make sure you got enough result to application for admission")
else:

    print("You are not eligable")