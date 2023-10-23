print("you are aging to play the fixxbuzz game here:")
a = int(input("enter themax nuber:"))
for i in range(1,a+1):
    if(i%3==0 and i%5==0):
        print("fixxbuzz")
    elif(i%3==0):
        print("fizz")
    elif(i%5==0):
        print("buzz")
    else:
        print(i)
