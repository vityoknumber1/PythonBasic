#Складання цифр

number = input("Введіть число: ")

def number_collaps(number):
    s = 0
    x = str(number)

    try:
        if int(number) == 0:
            raise Exception("Помилка! Число повинно бути більше 0")

        for i in range(0, len(x)):
            s = s + int(x[i])
        if len(str(s)) > 1:
            s = number_collaps(s)
        return s
    except ValueError:
        print("Помилка! Число повинно бути більше 0 або це не ціле число")
    except Exception as e:
        print(e)

if number_collaps(number) is not None:
    print("Сума цифр: ", number_collaps(number))