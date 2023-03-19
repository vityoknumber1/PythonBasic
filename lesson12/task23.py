#Цифровий лічильник

class Counter:

    def __init__(self, min_val, max_val, start, i: int=1) -> None:
        self.increm = i
        self.min_val = min_val
        self.max_val = max_val
        self.start = start
        if start < min_val or start > max_val:
            print("Number must be in range [min_val;max_val]")

    def increment(self):
        self.start += self.increm
        self.curr = self.start

    def current(self) -> int:
        return self.curr

count1 = Counter(0, 100, 63)
count1.increment()
count1.increment()
count1.increment()
print("Current value of counter: ", count1.current())