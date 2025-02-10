import sys
n = int(sys.argv[1])
m = int(sys.argv[2])
m1 = m +1; m2 = m -1 #Переменные для удобного счёта
arr = []; i = 1
for k in range(m1): #Заполнение массива
    if i <= n: 
        arr.append(i)
        i+=1
    else: 
        arr.append(1)
        i=2
k=0; i=0
trvl = [arr[0]]
while True: #Цикл, в котором считается следующее значение интервала при помощи остатка от деления
    if arr[(k+m2)%m1] not in trvl: 
        k+=m2; i+=1 
        trvl.append(arr[k%m1])
    else: 
        break
for j in range(len(trvl)):
    print(trvl[j],end="")