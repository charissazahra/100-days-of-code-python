len(str(12345))

#Type checking atau buat cek value atau variable nya itu pake type data apa

#String
print(type("abc"))

city = "jakarta"
print(type(city))

#Integer
motorcycle_plat_number = 23456
print(type(motorcycle_plat_number))

#Float
phi_segitiga = 3.14159
print(type(phi_segitiga))

#Boolean
is_ok = True
print(type(is_ok))

#Jenis-jenis Array
array_of_karakter = ['a','p','a','y','e']
print(type(array_of_karakter[0])) #notes: char

array_of_integer = [5678, 12345]
print(type(array_of_integer[1]))

array_of_float = [21.777, 55.55]
print(type(array_of_float[0]))

array_of_boolean = [True, False, True]
print(type(array_of_boolean[1]))

array_of_string = ["tulisan"]
print(type(array_of_string[0])) #Notes: array boleh punya cuma 1 value, yang berarti dia cuma punya 1 indeks doang

array_of_anything = ["cuba",12345, 66.6, True, 'j','a','c','k']
print(type(array_of_anything[2]))