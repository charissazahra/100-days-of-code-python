bill = int(input("what's your bill?: $"))
people = int(input("how many people?: "))
print("there is special discount 10% in here!")
discount = int(input("how much the discount?: %"))

bill_per_person = ((bill/people)*(100 - discount)/100)
print(bill_per_person)


