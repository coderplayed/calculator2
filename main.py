def cal():
 print("Welcome to Calculator \n")
 x = float(input("Enter the first number"))
 y = float(input("Enter the second number"))
 h = float(input("\nEnter the operation to be performed :\n"
                    "press 1 for Addition operation \n"
                    "press 2 for Subtration operation \n"
                    "press 3 for Multiplication operation\n"
                    "press 4 for Modulus operation \n"
                    "press 5 for Division operation \n"
                    "press 6 for Floor Division operation \n"
                    "press 7 for Exponent operation \n\n"))

 def add():
  a = x + y #Addition
  print(a)

 def sub():
  b = x - y #Subtration
  print(b)

 def mult():
  c = x * y #Multiplication
  print(c)

 def mod():
  d = x % y #Modulus
  print(d)

 def div():
  e = x / y #Division
  print(e)

 def flrdiv():
  f = x // y #Floor Division
  print(f)

 def exp():
  g = x ** y #Exponent
  print(g)

 if h == 1:
  add()

 elif h == 2:
  sub()

 elif h == 3:
  mult()

 elif h == 4:
  mod()

 elif h == 5:
  div()

 elif h == 6:
  flrdiv()

 elif h == 7:
  exp()

 else:
    mod()

 m = int(input("\nDo you wish to do another calculation?\n Press 1 if yes\n Press 2 if no\n"))
 if m==1:
    cal()

 elif m==2:
        print("Thank you for using the calculator")
 else:
        print("enter a valid choice")
        cal()

cal()

