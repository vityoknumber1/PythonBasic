#Бухгалтерська книга
list_of_lists = [
                    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
                    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
                    [77226, 'Head First Python, Paul Barry', 3, 32.95],
                    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
                ]

print(list_of_lists)

my_tuple = list(map(lambda x: (x[0], x[1], round((x[3] + 10), 2), x[2]) \
    if x[2] * x[3] < 100 else (x[0], x[1], x[3], x[2]), list_of_lists))

print("\nOrder number,", "Book title and author,", "Price per item,", "Quantity\n", my_tuple)