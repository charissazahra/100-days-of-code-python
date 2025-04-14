
money = int(input())
time = int(input())

if money > 10 and time < 10: #tanpa nested masukin time nya lgsg disini
    #if time < 10: #klo masukin time nya pake nested begini
    print("a")
if money < 10:
    if time > 10:
        print("b")
if time > 10:
    print("c")

# ada AND, OR
# a and b = ? false, NOTES: jika keduanya true, baru dia hasil nya true
# a = false, b = true

# a and b = ? true
# a = true, b = true

# a and b = ? false
# a = true, b = false

#OR bernilai true itu apa?
## a or b = ? true, NOTES: jika salah satunya true, itu udah pasti true
# a = false, b = true

#latihan nested
#if <condition 1 is false>
 #   <do A>    Note = ine 30 dan 34 di skip,jadi gaakan di eksekusi. lgsg ke line 35
  #  if <condition 2 is true>
   #     <do B>
    #    if <condition 3 is true>
     #       <do C>
#else:

#if itu harus ada (klo conditional check if itu hrs ada), head header
#elif itu sub header. note = elif atau else bisa conditional, bisa ada bisa gak
#else itu footer