import random

human_score = 0
pc_score = 0
round = 0

while round < 3:

    human = input ("sang , kaghaz , gheychi :")
    pc = ["sang" , "kaghaz" , "gheychi" ]
    pc_choise = (random.choice(pc))
    print ("entekhabe pc" ,pc_choise, "bood")

    if human == "sang" and pc_choise == "gheychi" :
        print ("human won")
        human_score += 1
    elif human == "kaghaz" and pc_choise == "sang" :
        print ("human won")
        human_score += 1
    elif human == "gheychi" and pc_choise == "kaghaz" :
        print ("human won")
        human_score += 1
    elif human == pc_choise :
        print ("mosavi")
    else :
        print ("pc won")
        pc_score += 1

    round += 1

print ("human score :",human_score)
print ("ps_sccore :",pc_score)

if human_score > pc_score :
    print ("human won")

elif human_score < pc_score :
    print ("pc won")

elif human_score == pc_score :
    print ("mosavi")