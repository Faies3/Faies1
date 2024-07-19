car=[]
car.extend(["honda","bmw","mercedes","toyota","audi"])
print(f"cars :{car} ")
car.insert(1,"volvo")
print(f"insertion of volvo :{car} ")
car.remove("bmw")
print(f"after removing bmw :{car} ")
popped_car=car.pop(-1)
print(f"popped_car : {popped_car}")
print(f"first element of car list :{car[0]}\nLast element of car list :{car[-1]}")
try:
    print(car[10])
except:
    print(f"index out of range .will will add ")
car.extend(["ford","chevrolet","nissan","kia","hyundai","mazda"])
print(f"after extending car list :{car} ")
for i in car:
    if i=="tesla":
        car.remove("tesla")
        break
    else:
        car.append("tesla")
        print(f"after inserting tesla :{car} ")
        break