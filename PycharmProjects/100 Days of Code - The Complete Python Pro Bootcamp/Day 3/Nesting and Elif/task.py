maths_score = int(input())
english_score = int(input())

if maths_score >= 90:
    if english_score >= 90:
        print("You're good at everything")
    else:
        print("You're good at maths")
elif english_score >= 90:
    print("You're good at english")

#jika score kedua nya 90 itu auto dapet youre good at everything.
#jika score salah satunya ada yg beda bukan 90 atau lebih dari 90,
#itu salah satu nya aja yg ke print antara else, atau elif nya tergantung dari score yg mana yg >=90 yg akan ke print.

