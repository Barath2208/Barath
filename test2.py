A=int(input("Enter the starting element: "))
B=int(input("Enter the ending value: "))
cube=[]
print("The cube of given elements are: ")
for i in range(A,B+1):
    c=i*i*i
    cube.append(c)
print(cube)
