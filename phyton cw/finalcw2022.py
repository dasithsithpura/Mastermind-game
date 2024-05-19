import random
import os

again=input("\n Are you reddy to play game (Yes/No): ")
if again=="yes" or again=="No":
            os.system('cls')
            value=0



name = str(input("Enter player Name:"))




print("\t       ""Hi",name,"Welcome to GameInt")

print("Number to Guess:xxxx""\t             ""Color Mapping:")

print("\t                                       ""1-White 2-Blue 3-Red")
print("\t                                       ""4-Yelllow 5-Green 6-Purple")


colors=["White","Blue","Red","Yellow","Green","Purple"]
print("------------------------------------------------------------------------")



num = random.sample(['1','2','3','4','5','6'], 4)

value=0
result=[]

while True: 
    guess=str(input("\nEnter the number :" )) 
    
    print("\t                                        attemp_no    guess   result")
   
    if guess == ("0000"):
      print("\n game over")
      print("\n\tThank Playing This Game \n\tplease enter Any Key To Exit.....")

   


    try:
       int(guess) 
    except:
        print("\nsorry you can input numbers only.")
        continue
        
    
    while not(len(guess)==4) or '7' in guess or '8' in guess or '9' in guess or '0' in guess:
        print("\n\tsorry you can input four numbers only.\n\tcheck your number and try again")
        guess=input('\nEnter the number again:')

    value=value+1        
    for i in range(4):
        if num[i]==guess[i]:
            result.append('1')
        else:
            result.append('0')
        
    score=int((8-value)/8*100)

    if result.count('1')==4:
        os.system('cls')


        print(f"\t                                             {value}       {guess}     {result[0]}{result[1]}")
        print(f"\t                                                              {result[2]}{result[3]}")
        print("\t                               __________________________________")
        
        print("\nCongratulations !!!!! You have won the game…")
        print(f'You have scored {score}% points.')
        result.clear()
        
        again=input("\nif you want to play again (Yes/No): ")
        if again=="yes" or again=="No":
            os.system('cls')
            value=0
            
            continue
        else:
            os.system('cls')
            print("\n\tThank for Playing This Game \n\tplease enter Any Key To Exit.....")
            input()
            os.system('cls')
            break

    elif value>8:
        os.system('cls')
        print(' Sorry! Maximum Attempts Have been Used')
        again=input("\nDo You want to play again (Yes/N0): ")
        if again=="yes" or again=="No":
            os.system('cls')
            value=0
            print("\t            ""HI", name , "Well come to the gameint")
            print("Number to Guess:2561""\t             ""Color Mapping:")
            print("\t                                       ""1-White 2-Blue 3-Red")
            print("\t                                 ""4-Yelllow 5-Green 6-Purple")
            print("-------------------------------------------------------------------------------")
            continue
        else:
            os.system('cls')
            print("\n\tThanks for the playing")
            input()
            os.system('cls')
            break
           


    else:

       
        print(f"\t                                             {value}       {guess}     {result[0]}{result[1]}")
        print(f"\t                                                              {result[2]}{result[3]}")
        print("\t                               __________________________________")

        result.clear()
        continue
