print("welcome to the world of pizza, sir")
print("how can i help you, sir")
print("we have three range of pizza,sir")
print("large(L), small(S) , mediam(M)")
bill = 0
pizza = (input("enter the range of pizza you want sir"))
if(pizza =="S"):
    bill = 15
    print("thank you it is of 15 doller sir")
if(pizza == "M"):
    bill = 20
    print("thank you sir it is of 25 doller")
if(pizza == "L"):
    bill = 25
    print("thank you sir it is of 25 doller")    
else:
    print("sorry sir there may be a problem regarding the you input sir try again sir ")

a = input("wnna add peporani for bizza sir if yes type (Y) if no type (N)")
if(a == "Y"):
    if(pizza == "S"):
        bill += 2
        print(f"you bill is now {bill}") 
    if(pizza == "L" or pizza == "M"):
        bill += 3
        print(f"your bill is now {bill}")     
    else:
        print("sorry sir invalid input")

print("do you wanna extra chees sir ")
b = input("type (Y) for yes or (N)") 
if(b == "Y"):
    bill += 1
    print(f"sir your final bill is {bill}")
print("thank you sir , i hope you will come again sir")    

