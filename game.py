name = str(input('Please enter ur name: '))
print ("Welcome ",name," to the addition game")
Num = int(input('how many questions would you like to answer? \n'))
total = 0
for i in range(0,Num,1):
    a= 2+i
    b=10+i
    print ('A = ',a,'\n B = ',b)
    ans = int(input("What is the sum of a and b: \n"))
    add = a + b
    if (ans == add):
        total = total + 1
print("Ur score is ",total,"out of",Num)
