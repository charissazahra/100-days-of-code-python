print("Welcome to Python Pizza Deliveries!")


#ini aku yg edit ulang

size_pizza = input("What size pizza do you want? S, M, or L: ")

pepperoni_on_pizza = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")


total_bill = 0


if size_pizza == "S": #true
    total_bill = total_bill + 15
    if pepperoni_on_pizza == "Y":
        total_bill = total_bill + 2

elif size_pizza == "M":
    total_bill = total_bill + 20
    if pepperoni_on_pizza == "Y":
        total_bill = total_bill + 3

elif size_pizza == "L":
    total_bill = total_bill + 25
    if pepperoni_on_pizza == "Y":
        total_bill = total_bill + 3

if extra_cheese == "Y":
    total_bill = total_bill + 1

print(f"Your final bill is: ${total_bill}.")
