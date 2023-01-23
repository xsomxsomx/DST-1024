import numpy as np

def number_prediction(number:int=1) -> int:
    """Угадываем число менее чем за 20 попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    low = 1
    high = 100
    
    while True:    # заходим в вечный цикл
        count += 1    # увеличиваем количество попыток на единицу
        predict_number = low + (high - low) // 2    # как предполагаемое число, берем середину нашего отрезка

        if number > predict_number:    # проверяем что загаданное число больше нашего предположения
            low = predict_number    # если больше, то левую границу сдвигаем и делаем ее равной нашему предполагаемому числу
        elif number < predict_number:    # если первое условие не сработало, проверяем что число меньше нашего предположения
            high = predict_number    # если условие верно, сдвигаем правую границу и делаем ее равной нашему предполагаемому числу
        else:    # если оба условия оказались ложны, то значит числа равны и мы угадали число
            break    # принудительно выходим из цикла
    
        if count > 20:    # это дополнительное условие, для того, чтобы не уйти в вечный цикл
            break
    return(count)

print(f'Количество попыток: {number_prediction()}')

def score_game(number_prediction) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        number_prediction ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(number_prediction(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(number_prediction)
