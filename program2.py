#program to see what weight yarn you have

wpi = int(input("Please enter your wraps per inch(wpi): "))
if wpi < 0:
    print("Invalid number")
elif wpi <= 4:
    print("You have Jumbo yarn")
    print("It is weight 7")
elif wpi <= 6:
    print("You have Super Bulky yarn")
    print("It is weight 6")
elif wpi <= 9:
    print("You have Bulky yarn")
    print("It is weight 5")
elif wpi <= 12:
    print("You have Medium yarn")
    print("It is weight 4")
elif wpi <= 15:
    print("You have Light yarn")
    print("It is weight 3")
elif wpi <= 18:
    print("You have Fine yarn")
    print("It is weight 2")
elif wpi <= 30:
    print("You have Super Fine yarn")
    print("It is weight 1")
else:
    print("You have Lace yarn")
    print("It is weight 0")