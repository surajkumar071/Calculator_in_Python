



SFS setting the stage of the day of the day of the day 








a = int(input("Enter First Number :- "))
b = int(input("Enter Second Number :- "))
list =['addition','subtraction','multiplication','divide']
c = input("Choose  operation : ")

for i in list:
    if (i == c):
        if(i == 'addition'):
            print(a+b)
            break
        elif(i == 'subtraction'):
            print(a-b)
            break
        elif(i == 'multiplication'):
            print(a*b)
            break
        else:
            print(a/b)
            break
else:  print("Operation not found !")
