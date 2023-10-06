print("welcome to the love calculater:")
name1 = input("what is your name:")
name2 = input("what is there name:")
c = name1 + name2
true_count =int(c.count("t")) + int(c.count("r")) + int(c.count("u")) + int(c.count("e"))
love_count = int(c.count("l")) + int(c.count("o")) + int(c.count("v")) + int(c.count("e")) 
int_total = str(true_count) + str(love_count)
total = int(int_total)
print(f"your love score is {total}")
if(total<10):
    print("worst couple")
elif(total>10 and total <50):    
    print("you are alright")
elif(total >50 and total <80):
    print("you are bawal yarrr")
else:
    print("best couple yarr sex karlo yahi per")    