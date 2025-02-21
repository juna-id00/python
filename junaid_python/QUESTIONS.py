Grade

x=int(input("enter the mark :"))
if x>100:
    print("invalid mark")
elif x >= 90 and x<= 100:
    print("A")
elif x >= 80 and x< 90:
    print("B")
elif x >= 70 and x< 80:
    print("C")
elif x>= 60 and x< 70:
    print("D")
else:
    print("FAIL")



Electricity Bill


x=int(input("enter the unit :"))
a=x-100
b=x-200
if x<=100:
    print("NO BILL")

elif x>100 and x<=200:
    print(a*5)
elif x>200:
    print(b*10+500)
else:
    print("INVALID UNIT")





Calculator


a=x-100
b=x-200
if x<=100:
    print("NO BILL")

elif x>100 and x<=200:
    print(a*5)
elif x>200:
    print(b*10+500)
else:
    print("INVALID UNIT")

x=int(input("ENTER x :"))
y=int(input("ENTER y :"))
z=int(input("ENTER THE NUMBER :"))
if z <= 4:
     
    if z == 1:
        print(x+y)
    elif z == 2:
        print(x-y)
    elif z == 3:
        print(x*y)
    elif z == 4:
        print(x/y)
else:
   print("invalid input")





method two 


x=int(input("enter the x :"))
z=input("Enter the Sign :")
y=int(input("enter the y :"))
if z == "+":
    print(x+y)
elif z == "-":
    print(x-y)
elif z == "*":
    print(x*y)
elif z == "/":
    print(x/y)
elif z == "%":
    print(x%y)
elif z == "**":
    print(x**y)
elif z == "//":
    print(x//y)
else:
    print("invalid input")





wap to reverse a num using while loop

n=int(input("enter the num: "))
rev=0
while n !=0:
    rem=n%10
    rev=rev*10+rem
    n//=10
print(rev)




create a list and print the largest among them


largest=x[0]
i=1
while i<len(x):
    if x[i]>largest:
        largest=x[i]
    i+=1

print(largest)







wap to reverse a num using while loop


n=int(input("enter the num: "))
rev=0
while n !=0:
    rem=n%10
    rev=rev*10+rem
    n//=10
print(rev)