print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#print(bill*tip)

bill_per_person = (bill / people)
print(bill_per_person)

payment = (bill_per_person * (tip+100)/100) #karna klo bayar full itu 100%, dan ada tip nya jadi ditambah 12%. terus baru di bagi 100
print(payment)

#cara menghitung BMI
#height = 1.65
#weight = 84

# Calculate the bmi using weight and height.
#bmi = weight / (height**2) krn tubuh manusia itu ada tinggi dan lebar nya jadi dikuadrat kan 2

#print(bmi)   #NOTES: HASIL RUN NYA ITU 30.853994
#print(round(bmi))

#NOTES: Hasil dari print(bmi) itu bilangan desimal^,
# kita bulatkan dgn round function, krn biar dibulatkan ke angka atasnya jika > 5
# atau dibulatkan ke angka bawahnya jika < 5
# knp kita gapake int function aja? krn gak membulatkan angka hasil bmi,
# itu cuma menghilangkan koma nya

#contoh round function lainnya
#print(round(bmi, 2))
#NOTES: Hasil yang tadinya 30.853994, menjadi 30.85 saja
#soalnya angka 2 diatas itu, mengambil 2 angka setelah koma dari 30.853994 yaitu 30.85
