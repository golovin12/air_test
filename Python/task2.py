import timeit
import random


def func1(*args):
    result = []
    for sequence in args:
        result.extend((item, item ** item) for item in sequence)
    return result


def func2(sequence):
    return [item[1] for index, item in enumerate(sequence) if index == 0 or sequence[index - 1] != item]


# Для оптимизации можно первую функцию превратить в генератор и передавать его во вторую функцию
# Таким образом, можно будет обойтись без хранения в памяти длинного списка
# Пр:

def gen1(*args):
    for sequence in args:
        for item in sequence:
            yield (item, item ** item)


def new_func2(gen):
    result = []
    for item in gen:
        if len(result) == 0 or item[1] != result[-1]:
            result.append(item[1])
    return result


def main():
    list_input = [(1, 1), (2, 3), (2,), (2,)]

    result1 = func2(func1(*list_input))
    print(result1)

    result2 = new_func2(gen1(*list_input))
    print(result2)

    # Проверка резльтатов оптимизации
    time1, time2 = 0, 0
    for k in range(100):
        list_input = [[random.randint(1, 10) for j in range(random.randint(1, 15))] for i in range(1000)]

        t = timeit.default_timer()
        func2(func1(*list_input))
        time1 += timeit.default_timer() - t

        t = timeit.default_timer()
        new_func2(gen1(*list_input))
        time2 += timeit.default_timer() - t

    print("После оптимизации время выполнения функции, в среднем, снизилось на",
          round(100 - 100 / time1 * time2, 2), "%")


if __name__ == "__main__":
    main()
