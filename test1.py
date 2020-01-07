A=int(input("Enter the starting element: "))
B=int(input("Enter the ending value: "))
Even=[]
Odd=[]
print("The even numbers are: ")
for i in range(A,B+1):
    if(i%2==0):
        Even.append(i)
print(Even)
print("The odd numbers are: ")
for i in range(A,B+1):
    if(i%2!=0):
        Odd.append(i)
print(Odd)
