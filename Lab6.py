name = input("What is your name?:")
age = int(input("What is your age?:"))
if age >= 20:
  print("Hello", name + "! Welcome to our Lab 6 python program! You are so old.")
elif age < 20 and age >= 1:
    print("Hello", name + "! Welcome to our Lab 6 python program! You are young and energetic.")
elif age == 0:
    print("Hello", name + "! Welcome to our Lab 6 python program! I'm not sure how you are even\ninteracting with this at such a young age...I'm impressed!")
else:
    print("Hello", name + "! Welcome to our Lab 6 python program! You have a negative age and\ntherefore have not been born yet, so I'm not exactly sure who I'm talking to right now.")
