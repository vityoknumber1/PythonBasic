#Buffer
class Buffer:
    def __init__(self):
        # конструктор без аргументів
        self.num = []

    def add(self, *a):
        # добавити наступну частину послідовності
        self.num.extend(a)
        while len(self.num) >= 5:
            cur_s = 0
            for i in range(5):
                cur_s += self.num.pop(0)
            print("Сума поточної п'ятірки чисел:",cur_s)

    def get_current_part(self):
        # повернути суму п'яти збережених елементів послідовності
        return self.num

if __name__ == "__main__":
    buf = Buffer()
    buf.add(5, 5, 6)
    buf.get_current_part()
    buf.add(1, 11, 5, 8, 6, 4)
    buf.get_current_part()
    buf.add(1, 2)
    buf.get_current_part()
    buf.add(1, 2, 3, 4)
    buf.get_current_part()
    buf.add(15, 24, 45, 89)
    buf.get_current_part()