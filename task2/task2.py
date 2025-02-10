import sys
def get_center_circle(arg): #Функция для получения координаты центра окружности и радиус
    with open(arg) as fp:
        center = fp.readline().split()
        x = int(center[0])
        y = int(center[1])
        r = int(fp.readline())
    return x, y, r
def get_points(arg): #Функция для получения координат точек
    points = []
    with open(arg) as fp:
        for line in fp:
            x,y=map(int, line.split())
            points.append((x,y))
    return points
def get_position(x,y,center_x,center_y,radius): #Функция для нахождения точек относительно окружности
    distance_square = ((x - center_x)**2 +(y - center_y)**2)
    radius_square = radius**2
    if distance_square < radius_square:
        return "1"
    elif distance_square > radius_square:
        return "2"
    else:
        return "0"
def main():
    data1 = sys.argv[1] #Объявление путей к файлам
    data2 = sys.argv[2]
    center_x, center_y, radius = get_center_circle(data1)
    points = get_points(data2)
    for x,y in points:
        print(get_position(x,y,center_x,center_y,radius))
if __name__ == "__main__":
    main()