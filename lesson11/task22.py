#Записати текстовий файл

file = open("file with input text.txt", "w+")
print("Enter the text: ")

lines = []

while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

text = '\n'.join(lines)
file.write(text)
file.close()
