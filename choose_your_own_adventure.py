name = input("Type you name: ")
print("Welcome", name, "to this adventure!")


answer = input("You are on a dirt road, it has come to an end and you can go left or right . Which way would you like to go? (left,right)").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across : ").lower()

    if answer == "swim":
        print("You swam across but were eaten by an alligator midway . You lost")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game ")
    else :
        print("Not a valid option. You lose. ")    

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back) ").lower()
    
    
    if answer == "back":
        print("You go back and a samurai comes from no where and kills you with his sword you lose (life is unfair)")
    elif answer == "cross":
        answer = input("You cross the bridge successfully despite it being wobbly and then after crossing you meet a stranger. Do you want to talk ? (yes/no) ").lower()


        if answer == "yes":
            print("You talk to the stranger and they give you gold and you win ")
        elif answer == "no":
            print("You ignore the stranger and they are offended and they kill you , you lose")
    else :
        print("Not a valid option. You lose. ")   
    
else:
    print("Not a valid option you lose.")    


