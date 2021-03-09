money = int(input())
money_used = money
dict_animals = {"sheep":[6769, "sheep"],"cow":[3848, "cows"],"pig":[1296,"pigs"],"goat":[678,"goats"],"chicken":[23,"chickens"]}  
val = []
for key, val in dict_animals.items():
    if money_used >= int(val[0]):
        qty = int(money_used / int(val[0]))
        if qty > 1:
            print(str(qty) , val[1])
            money_used -= int(val[0]) * qty
            break
        elif qty == 1:
            print(str(qty) , key) 
            money_used -= int(val[0])
            break
if money == money_used:
    print(None)
