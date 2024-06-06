import random
import os
os.system('cls')
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_card1_no = random.randint(0,12)
user_card2_no = random.randint(0,12)

pc_card1_no = random.randint(0,12)
pc_card2_no = random.randint(0,12)

user_card = [cards[user_card1_no], cards[user_card2_no]]

pc_card = [cards[pc_card1_no], cards[pc_card2_no]]

print(f"your cards are [ {user_card[0]} ] & [ {user_card[1]} ]")
print(f"Dealer cards are [ {pc_card[0]} ] & [ ? ]")


user_total = sum(user_card)

#initial checking
if user_total > 21:
    os.system('cls')
    print(f"Your cards {user_card} : {user_total} > 21 \nDealer cards ")
    print("Opps! Dealer has won, you had lost.")
    quit()

#if >21 asking for hit or stand action
continue_ = input("press ' h ' to hit or any key to stand: ")
if continue_ == "h":
     user_card.append(cards[random.randint(0,12)])

#checking after an hit
if user_total > 21:
    os.system('cls')
    print(f"Your cards {user_card} : {user_total} > 21 \nDealer cards {pc_card}")
    print("Opps! Dealer has won, you had lost.")
    quit()

    

#smaking dealer card sum greater than 17 too
while sum(pc_card) < 17:
    pc_card.append(cards[random.randint(0,12)])
pc_total = sum(pc_card)

#final output comparisions
if pc_total > 21:
    os.system('cls')
    print(f"Your cards {user_card}\nDealer cards {pc_card} : {pc_total} > 21 ")
    print("Congratulations! you have won.")
elif user_total == pc_total:
    os.system('cls')
    print(f"Your cards {user_card} : {user_total} \nDealer cards {pc_card} : {pc_total} ")
    print("Draw")
elif pc_total > user_total:
    os.system('cls')
    print(f"Your cards {user_card} : {user_total} \nDealer cards {pc_card} : {pc_total} ")
    print("Opps! Dealer has won, you had lost.")
else:
    os.system('cls')
    print(f"Your cards {user_card} : {user_total} \nDealer cards  : {pc_total} ")
    print("Congratulations! you have won.")

    