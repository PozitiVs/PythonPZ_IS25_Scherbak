#даны средние значения температур по месяцам. Найти минимальное и максимальное значение температур за год.
#Вывести значения температур по временам года
from functools import reduce

prepare_inp = lambda: list(map(float, input("Введите 12 температур через пробел: ").split()))
get_ex = lambda temps: (reduce(min, temps), reduce(max, temps))
seasons_st = lambda temps: (
    ('Зима', ['Дек','Янв','Фев'], [temps[-1], *temps[:2]]),
    ('Весна', ['Март','Апр','Май'], temps[2:5]),
    ('Лето', ['Июнь','Июль','Авг'], temps[5:8]),
    ('Осень', ['Сен','Окт','Нояб'], temps[8:11])
)

y_results = lambda extremes, seasons: (
    print(f"\nMin: {extremes[0]}\nMax: {extremes[1]}\n"),
    list(map(
        lambda s: print(f"{s[0]}: {', '.join(f'{m} {t}' for m, t in zip(s[1], s[2]))}"),
        seasons
    ))
)

(lambda: y_results(
    get_ex(temps := prepare_inp()),
    seasons_st(temps)
))()