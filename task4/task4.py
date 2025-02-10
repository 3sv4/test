import sys
arr = sys.argv[1]
nums = []
with open(arr, "r" ,encoding='utf-8') as file: #Чтение и запись файла(в переменную)
    nums = [int(line.strip()) for line in file]
x = 0
av = sum(nums)/len(nums)#Нахождение среднего числа к которому нужно привести число
nums.sort()
while nums[0] != nums[len(nums)-1]: #Цикл с пошаговой сортировкой,прибавлением,убавлением
    if nums[len(nums)-1] - av > av - nums[0]:
        x+=1
        nums[len(nums)-1]-=1
    else:
        x+=1
        nums[0]+=1
    nums.sort()
print(x)