import random
def computerchoice():
    computerchoice=["stone","papper","scissor"]
    getcompchoice=random.choice(computerchoice)
    print(f"Computer choice:{getcompchoice}")
    return getcompchoice
def userchoice():
    userchoice=input("User Choice:").lower()
    return userchoice

def gamerule(user,computer):
    if user==computer:
        print("Match draw")
        return "draw"
        
#user wins
    elif(user=="stone" and computer=="scissor")or\
        (user=="scissor" and computer=="papper")or\
        (user=="papper" and computer=="stone"):
          print("user wins")
          return "user"
          
#computer wins

    elif(user=="scissor" and computer=="stone")or\
        (user=="papper" and computer=="scissor")or\
        (user=="stone" and computer=="papper"):
        print("computer wins")
        return "computer"

userwins=0
compwins=0
draw=0

for i in range(6):
    print(f"\nRound {i+1}:")

    result=gamerule(user=userchoice(), computer=computerchoice())

    if result=="user":
      userwins=userwins+1
    elif result=="computer":
       compwins==compwins+1
    elif result=="draw":
       draw=draw+1
print("nfinal Result:")
print(f"User Wins:{userwins}")
print(f"Computer Wins:{compwins}")
print(f"Draws:{draw}")





if userwins>compwins:
    print("Overall winner is user")
elif compwins<userwins:
    print("Overall winner is computer")
else:
    print("Match is tie")











