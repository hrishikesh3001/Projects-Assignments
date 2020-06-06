nterms = int(input("Enter no.of terms :  "))

a, b = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(a)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(a)
       x = a + b
       a = b
       b = x
       count += 1
