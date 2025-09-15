a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
list =['add','sub','multiply','divide']
c = input("Choose  operation : ")

for i in list:
    if (i == c):
        if(i == 'add'):
            print(a+b)
            break
        elif(i == 'sub'):
            print(a-b)
            break
        elif(i == 'multiply'):
            print(a*b)
            break
        else:
            print(a/b)
            break
else:  print("Operation not found !")
