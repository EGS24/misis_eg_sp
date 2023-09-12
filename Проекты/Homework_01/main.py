import math
import datetime


def exercise_01():
    def in_put():
        print("Задание 1.")
        number = int(input("Введите число:"))
        return number

    def amount(number):
        return (number * (number + 1)) / 2

    num = in_put()

    def main_01(number):
        print(amount(number))

    main_01(num)


def exercise_02():
    def in_put():
        print("Задание 2.")
        a = int(input("Введите первое число:"))
        b = int(input("Введите второе число:"))
        return a, b

    def print_exercise(a, b):
        print("Арифметические операции:")
        print("Сложение a и b:", a + b)
        print("Разность a и b:", a - b)
        print("Произведение a и b:", a * b)
        print("Частное от деления a на b:", round(a / b, 2))
        print("Целочисленное деление a на b:", a // b)
        print("Остаток от деления a на b:", a % b)
        print("Возведение числа a в степень b:", a ** b)
        print("Десятичный логарифм числа a:", round(math.log10(a), 2))
        print("Операции сравнения:")
        print("a < b", a < b)
        print("a <= b", a <= b)
        print("a > b", a > b)
        print("a >= b", a >= b)
        print("a != b", a != b)
        print("a == b", a == b)

    num_1, num_2 = in_put()

    def main_02(num_01, num_02):
        print_exercise(num_01, num_02)

    main_02(num_1, num_2)


def exercise_03():
    def in_put():
        print("Задание 3.")
        x = int(input("Введите первое число: "))
        y = int(input("Введите второе число: "))
        z = int(input("Введите третье число: "))
        return x, y, z

    num_01, num_02, num_03 = in_put()

    def entry(num_1, num_2, num_3):
        print(round((((num_1 ** 5 + 7) / abs(-6) * num_2) ** (1 / 3)) / (7 - num_3 % num_2), 3))

    def main_03(num_1, num_2, num_3):
        entry(num_1, num_2, num_3)

    main_03(num_01, num_02, num_03)


def exercise_04():
    def in_put():
        print("Задание 4.")
        a = float(input("Сопротивление первого проводника: "))
        b = float(input("Сопротивление второго проводника: "))
        return a, b

    num_1, num_2 = in_put()

    def amount(num_01, num_02):
        return num_01 + num_02

    def main_04(num_01, num_02):
        print("Сопротивление цепи равно: {}".format(round(amount(num_01, num_02), 1)))

    main_04(num_1, num_2)


def exercise_05():
    def in_put():
        print("5 задание.")
        a = int(input("Введите a: "))
        b = int(input("Введите b: "))
        m = int(input("Введите m: "))
        n = int(input("Введите n: "))
        return a, b, m, n

    num_01, num_02, lower_limit, upper_limit = in_put()

    def entry(num_1, num_2):
        return (-num_2) / num_1

    def main_05(num_1, num_2, low_lim, up_lim):
        print(low_lim <= entry(num_1, num_2) <= up_lim)

    main_05(num_01, num_02, lower_limit, upper_limit)


def exercise_06():
    def in_put():
        print("Задание 6.")
        v = int(input("Введите скорость:"))
        t = int(input("Введите время:"))
        max_kil = 122
        return v, t, max_kil

    num_v, num_t, num_max_kil = in_put()

    def entry(v_1, t_1, max_1):
        print("Спортсмен остановится на {} километре.".format(v_1 * t_1 % max_1))

    def main_06(v_1, t_1, max_1):
        entry(v_1, t_1, max_1)

    main_06(num_v, num_t, num_max_kil)


def exercise_07():
    def in_put():
        print("Задание 7.")
        a = int(input("Введите двузначное число:"))
        b = int(input("Введите трехзначное число:"))
        return a, b

    num_1, num_2 = in_put()

    def amount(one, two):
        sum_a = one // 10 + one % 10
        umn_a = (one // 10) * (one % 10)
        sum_b = two // 100 + two // 10 % 10 + two % 10
        umn_b = (two // 100) * (two // 10 % 10) * (two % 10)
        print(f"Сумма двузначного числа: {sum_a}")
        print(f"Произведение двузначного числа: {umn_a}")
        print(f"Сумма трехзначного числа: {sum_b}")
        print(f"Произведение трехзначного числа: {umn_b}")

    def main_07(num_1_, num_2_):
        amount(num_1_, num_2_)

    main_07(num_1, num_2)


def exercise_08():
    def in_put():
        print("Занятие 8.")
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = int(input("Введите третье число: "))
        return a, b, c

    num_1, num_2, num_3 = in_put()

    def entry(one, two, three):
        minimum = min(one, two, three)
        maximum = max(one, two, three)
        middle = one + two + three - minimum - maximum
        print(minimum, middle, maximum)

    def main_08(num_1_, num_2_, num_3_):
        entry(num_1_, num_2_, num_3_)

    main_08(num_1, num_2, num_3)


def exercise_09():
    def in_put():
        print("Занятие 9.")
        a = int(input("Введите первое число:"))
        b = int(input("Введите второе число:"))
        return a, b

    num_1, num_2 = in_put()

    def change(one, two):
        two += one
        one = two - one
        two -= one
        return one, two

    num_1_after, num_2_after = change(num_1, num_2)

    def main_09(num_01, num_01_after, num_02, num_02_after):
        print("Первое число до: {}, и после: {}. Второе число до: {}, и после: {}."
              .format(num_01, num_01_after, num_02, num_02_after))

    main_09(num_1, num_1_after, num_2, num_2_after)


def exercise_10():
    def in_put():
        print("Занятие 10.")
        name = str(input("Введите название футбольной команды:"))
        print(name + " - чемпион!")
        return name

    name_fut = in_put()

    def operations(name):
        print("-" * len(name))
        print("Длина наименования команды:", len(name.lower()))
        print("Есть ли в наименовании команды буква 'п'?", 'п' in name)  # как здесь получить True/False?
        print("Буква 'а' повторяется:", name.count("а"))

    def main_10(name):
        operations(name)

    main_10(name_fut)


def exercise_11():
    def in_put() -> tuple[str, str]:
        print("Занятие 11.")
        country = str(input("Введите название государства:"))
        capital = str(input("Введите название столицы:"))
        return country, capital

    country_entry, capital_entry = in_put()

    def entry(name_country, name_capital):
        print("Государство - {}, столица - {}".format(name_country, name_capital))

    def main_11(name_country, name_capital):
        entry(name_country, name_capital)

    main_11(country_entry, capital_entry)


def exercise_12():
    print("Задание 12.")
    word = "объектно-ориентированный"

    def entry(word_1):
        print("Слово:{}".format(word_1[:6]))
        print("Слово:{}".format(word_1[9:17]))
        print("Слово:{}".format(word_1[14:17]))
        print("Слово:{}".format((word_1[4] + word_1[0] + word_1[5])))
        print("Слово:{}".format((word_1[10] + word_1[3] + word_1[6] + word_1[5] + word_1[19])))

    def main_12(word_1):
        entry(word_1)

    main_12(word)


def exercise_13():
    print("Задание 13.")
    a = []
    b = []
    a.append(4.5)
    a.append(3.4)
    a.extend([8.7, 1.3])
    b.append(14.5)
    b.append(3.4)
    b.extend([8.7, 11.3])
    a.insert(1, 100)
    a.insert(3, 100)
    b.insert(0, 200)
    b.insert(2, 200)
    print(f"\nИсходные списки:\n a = {a},\n b = {b}")
    del a[0]
    del b[0]
    a.remove(100)
    b.remove(200)
    print(f"\nПосле удалений:\n a = {a},\n b = {b}")
    sa = set(a)
    sb = set(b)
    sa_and_sb = sa & sb
    print("\nУникальные элементы:")
    print("1-й: ", sa)
    print("2-й: ", sb)
    print("Общие:", sa_and_sb)
    c = a + b
    c_asc = sorted(c)
    c_desc = sorted(c, reverse=True)
    c_even = list(c[1::2])
    sr_ar = sum(c_even) / len(c_even)
    c_odd = list(c[::2])
    sr_geom = round(math.prod(c_odd) ** (1 / len(c_odd)), 2)

    c_max = max(c)
    c_min = min(c)

    print("\nИтоговые:")
    print("3-й:", c)
    print("Сортировка (возр.):", c_asc)
    print("Сортировка (убыв.):", c_desc)
    print("Ср. арифм. = {}, ср. геометр. = {}.".format(sr_ar, sr_geom))
    print("Макс. и мин.:", c_max, c_min)


def exercise_14():
    print("Занятие 14.")
    info = dict()
    info["фио"] = "Иванов Иван Иванович"
    info["дата_рождения"] = "24.09.1997"
    info["место_рождения"] = "Москва"
    print(info)
    info["хобби"] = ["плавание", "хоккей", "футбол"]
    info["хобби"].append("программирование")
    info["животные"] = ("кошка Мурка", "собака Найда")
    info["ЕГЭ"] = dict()
    info["ЕГЭ"]["математика"] = 100
    info["ЕГЭ"]["информатика"] = 50
    info["ЕГЭ"]["русский"] = 0
    info["ЕГЭ"].pop("русский")
    info["вузы"] = dict()
    info["вузы"]["МИСИС"] = 40
    info["вузы"]["МГТУ им. Н.Э.Баумана"] = 50
    print("Данные:")
    print(info)
    exams = tuple(sorted(info["ЕГЭ"].keys()))
    print("Предметы:", *exams)
    uni = sorted(info["вузы"].keys())
    print("Вузы:", *uni)
    print("\nОтветы на вопросы:")
    name = info["фио"].split()[1]
    start_vowel = name[0].lower() in "аоуыэяёюие"
    print("* мое имя начинается на гласную букву:", start_vowel)
    date_time_obj = datetime.datetime.strptime(info["дата_рождения"], '%d.%m.%Y')
    month = date_time_obj.month
    born_winter_or_summer = month in [12, 1, 2, 6, 7, 8]
    print("* родился летом или зимой:", born_winter_or_summer)
    hobbies_count = len(info['хобби'])
    print("* у меня {} хобби, первое \"{}\"".format(hobbies_count, info['хобби'][0]))
    exams_count = len(info['ЕГЭ'])
    print("* после окончания школы сдавал {} экз.".format(exams_count))
    sum_marks = sum(info['ЕГЭ'].values())
    print("* сумма баллов = {}".format(sum_marks))
    max_mark = max(info['ЕГЭ'].values())
    print("* макс. балл = {}".format(max_mark))
    vuz_count = sum(points <= sum_marks for points in info["вузы"].values())
    print("* кол-во вузов в которые прохожу: {}".format(vuz_count))


def main():
    exercise_01()
    exercise_02()
    exercise_03()
    exercise_04()
    exercise_05()
    exercise_06()
    exercise_07()
    exercise_08()
    exercise_09()
    exercise_10()
    exercise_11()
    exercise_12()
    exercise_13()
    exercise_14()


main()
