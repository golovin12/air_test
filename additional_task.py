# В качестве подхода к решению задачи я выбрал жадный алгоритм
# Т.е. пытаюсь распределить бег между участками, где у меня самая низкая скорость
def get_variables_from_file(file_name):
    with open(file_name) as file:
        X, S, R, t, N = list(map(lambda y: int(y),file.readline().split(" ")))
        # print([X, S, R, t, N])
        args = list(map(lambda x: list(map(lambda y: int(y), x.split(" "))), file.readlines()))
        # print(args)
        return [X, S, R, t, N, *args]


def minimum_time(X, S, R, t, N, *args):
    speed = [S] * X

    for i in args:
        for j in range(i[0], i[1]):
            speed[j] = [i[2], speed[j]]

    my_shagi = speed.count(S) # Количество метров без дорожек
    my_dorogs = {} # Словарь где ключ - скорость дорожки, а значение - количество метров таких дорожек

    for item in speed:
        if isinstance(item, list):
            my_dorogs[item[0]] = my_dorogs.get(item[0], 0) + 1

    dlina1 = R * t - my_shagi
    # Проверяю, могу ли я затратить бег не наступая на дорожки
    if dlina1 > 0:
        # Если остались лишние секунды, то трачу их на дорожки от медленных к более быстрым
        t = dlina1 / R
        time_in_doroga = my_shagi / R
        time_in_plato = 0
        for item in sorted(my_dorogs.items()):
            if t > 0:
                dlina2 = (R + item[0]) * t - item[1]
                # проверяю, могу ли я затратить бег на дорожки с выбранной скоростью
                if dlina2 > 0:
                    t = dlina2 / (R + item[0])
                    time_in_plato += item[1] / (R + item[0])
                else:
                    time_in_plato += t + (-dlina2) / (item[0] + S)
                    t = 0
            else:
                time_in_plato += item[1] / (item[0] + S)
    else:
        time_in_doroga = t + (-dlina1) / S
        time_in_plato = sum([item[1] / (item[0] + S) for item in my_dorogs.items()])
    return time_in_doroga + time_in_plato

def main():
    file_name = "input.txt"
    variables = get_variables_from_file(file_name)
    answer = minimum_time(*variables)
    print("Минимальное число секунд:", answer)

if __name__ == "__main__":
    main()
# print(minimum_time(10, 1, 4, 1, 2, (4, 6, 1), (6, 9, 2)))
# print(minimum_time(12, 1, 2, 4, 1, (6, 12, 1)))
# print(minimum_time(20, 1, 3, 20, 5, (0, 4, 5), (4, 8, 4), (8, 12, 3), (12, 16, 2), (16, 20, 1)))
