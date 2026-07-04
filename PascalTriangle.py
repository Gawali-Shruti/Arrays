n=int(input("Enter Number of rows :"))
triangle=[]

for i in range(n):
    row=[1]*(i+1)

    for j in range(1,i):
        row[j]=triangle[i-1][j-1]+triangle[i-1][j]
    triangle.append(row)

for row in triangle:
    for num in row:
        print(num,end=" ")

    print()    

