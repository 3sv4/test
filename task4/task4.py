import sys
arr = sys.argv[1]
nums = []
with open(arr, "r" ,encoding='utf-8') as file: #Чтение и запись файла(в переменную)
    nums = [int(line.strip()) for line in file]
av = round(sum(nums)/len(nums))#Нахождение среднего числа к которому нужно привести число(привожу число к большему значению в случае .5)
number = 0
for x in range(len(nums)): #В цикле прохожусь по всем значениям и привожу к одному числу
    if nums[x] > av:
        number+= nums[x]-av
    elif nums[x] < av:
        number+= av-nums[x]
print(number)