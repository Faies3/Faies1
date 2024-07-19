Students=[]
for i in range(10):
    name=input(f"enter the {i+1}  element :")
    Students.append(name)
    print(Students)
Students.insert(3,"zera")
Students.remove("david")
popped=Students.pop(6)
print(f"popped Student is : {popped} ")
print(Students[1],Students[4])
Students.extend(["Karen","leo","mona","nina","oscar","paul"])
print(f"Entire list : {Students}")
for i in Students:
    if i=="victor":
        Students.remove("victor")
    else:
        Students.append("victot")
        break
print(Students)