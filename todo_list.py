task=[]
while True:
    print(f"1.add task \n2.show list\n3.exit")
    ch=int(input("enter your choice : "))
    if ch==1:
        inp=input("type your task :")
        task.append(inp)
    elif ch==2:
        for i in task:
            print(i)
    else:
        break