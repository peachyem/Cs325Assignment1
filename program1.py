#program to see if a user has enough yarn for a project by converting yards to meters

yards = int(input("Enter your yardage: "))
patternmeters = int(input("Enter your pattern requirements in meters: "))
meters = yards / 1.094
>>>>>>> a3d53930ad21a63fa20cffdebd24d8df900d03e0
if(meters > patternmeters):
    print("You have enough yarn:)")
else:
    print("You don't have enough yarn :(((((((((")
    
