import random
#to choose random numbers
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice:1.s 2.w 3.g :")
youDict = {"s": 1, "w": -1, "g": 0} #to convert string to number
reverseDict = {1: "Snake", -1: "Water", 0:"Gun"} #to convert number to string

you = youDict[youstr]

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer == you): #when both choose the same option
    print("Its a draw")
else:
    #conditions: when you will win
    if(computer==1 and you==0) or \
      (computer==0 and you==-1) or \
      (computer==-1 and you==1):
      print("YEAHH!! You win.!")
    #conditions: when you will loose
    else:
       print("oops! You lose.!")
