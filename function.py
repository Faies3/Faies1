
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

while True:
    main_1=int(input(f"1 :addition \n2 :substraction \n3 : multiplication \n4 : division :" ))
    if main_1==1:
         a=int(input("enter the 1st number :"))
         b=int(input("enter the second number :"))
         print(add(a,b))
         break
    elif main_1==2:
        a=int(input("enter the 1st number :"))
        b=int(input("enter the second number :"))
        print(sub(a,b))
        break
    elif main_1==3:
        a=int(input("enter the 1st number :"))
        b=int(input("enter the second number :"))
        print(mul(a,b))
        break
    elif main_1==4:
        a=int(input("enter the 1st number :"))
        b=int(input("enter the second number :"))
        print(div(a,b))
        break
    else:
        print("invalid input")
        break
  
