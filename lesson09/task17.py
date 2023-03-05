#Розгорнутий вигляд числа

number = input("Введіть число: ")

def expanded_form(number):

    try:
        if int(number) == 0:
            raise Exception("Помилка! Число повинно бути більше 0")

        res = []

        for index, digit in enumerate(str(int(number))[::-1]):
            if int(digit) != 0:
                res.append(digit + ("0" * index))

        return print(' + '.join(res[::-1]))

    except ValueError:
        print("Помилка! Число повинно бути більше 0 або це не ціле число")
    except Exception as e:
        print(e)

expanded_form(number)