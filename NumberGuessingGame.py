import random
import math

lower=int(input("Enter the lower bound of the Number "))
upper=int(input("Entet the upper bound of the Number "))

x=random.randint(lower,upper)

guess=round(math.log(upper-lower+1,2))

ogg=guess

print("Minimum number of Guess will be ", guess)

#print("Ranmdom is ",x)

while guess>0:
    print("",guess," try left")
    a=int(input("Enter the desired number "))
    
    if a==x:
        print("You have enter the the correct number")
        print("You have done in ",ogg-guess," try")
        break
    if a>x:
        print("Too high, please try other number")
    if a<x:
        print("Too Low, please try other number")
    guess=guess-1
    
if guess==0:
    print("You have passed the Limit of number of guess")