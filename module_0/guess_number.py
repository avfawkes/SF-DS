import numpy as np

def game_core_v3(number):
    ''' Функция принимает загаданное число и возвращает число попыток.
        Изначально проверяется среднее число из возможного диапазона 1-100.
        На каждой следующей итерации, в зависимости от результата сравнения, диапазон сужается сверху или снизу.'''
    count = 1
    predict = 50
    lower_band = 0
    upper_band = 101
    
    while number != predict:
        count+=1
        if number > predict: 
            lower_band = predict
            predict += (upper_band-lower_band)//2
        elif number < predict: 
            upper_band = predict
            predict -= (upper_band-lower_band)//2
    return(count) # выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(538)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v3)