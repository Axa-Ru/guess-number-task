#!/usr/bin/env python3

"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict2(number: int = 1) -> int:
    """ Угадываем число методом дихотомии.
        Вычисляем предполагаемое число, как среднее между верхней и нижней границей.
          Если
            предполагаемое число больше,
              то нижняя граница приравнивается предпологамому числу;
            предполагаемое число меньше,
              то верхняя граница приравнивается предпологамому числу;
            если равны - ок. мы нашли его.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count: int = 0
    bottom = 1
    upper = 101

    while True:
        count += 1
        # сумма может быть нечетная - округляем
        predict_number = int((upper + bottom) / 2)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла, если угадали
        if number > predict_number:
            bottom = predict_number
        else:
            upper = predict_number

    return count


def score_game(random_predict2) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict2 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict2(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    score_game(random_predict2)
