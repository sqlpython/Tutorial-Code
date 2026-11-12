import math
print("\033c", end="")
print("Make lemonade")
# print(input:
water_liters  = int(input("Enter liters of water : "))
sugar_grams = int(input("Enter grams of sugar : "))


min_water_per_serv = 500
min_sugar_per_serv = 100

if  ((sugar_grams) < (water_liters / 5 )) or water_liters < 500 :
    print( "low water or sugar No lemonade" )
"""  
elif water_liters < 500 :
    print("Low water can't make lemonade")
    clear
elif print("let's make some Lemonade") """

servings = int (water_liters // 500 )
if sugar_grams < (water_liters / 5):
    print ("Not enough sugar to make lemonade")
elif sugar_grams >= water_liters / 5:
    print(f" Makes {servings} 500 liters servings for your enjoyment ")
 
