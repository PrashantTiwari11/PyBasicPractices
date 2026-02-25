x = float(input("Enter the first number for operation : "))
y = float(input("Enter the second number for operation : "))
print ("""Choose From 1 to 4
       1. Addition
       2. Substraction
       3. Multiplication
       4. Division """)
choice = int(input("Enter your choice: "))
if choice == 1:{
    print (f"Addition is {x + y}")}
elif choice == 2: {
    print (f"Substraction is {x - y}")}
elif choice == 3 :{
    print (f"Multiplication is {x * y}")}
elif choice == 4:
    if y!=0: {
    print (f"Division is {x / y}")}
    else : print("Division can't done just beacuse your y value is 0.")
    
else:
    print ("Please choose correct choice ")
