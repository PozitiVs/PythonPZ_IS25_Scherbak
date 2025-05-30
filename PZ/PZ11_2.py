#из предложенного текстового файла (18-31) вывести на экран
#его содержимое, кол-во символов принадлежащих к группе букв.
#сформировать новый файл в который поместить строку наименьшей длины.
inp_filename = '18-31.txt'
out_filename = 'short_line.txt'

with open(inp_filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()

print("Содержимое файла:")
for line in lines:
    print(line)

letter_count = 0
for line in lines:
    for ch in line:
        if ch.isalpha():
            letter_count += 1

print(f"\n Количество букв в файле: {letter_count}")

if lines:
    short_line = min(lines, key=len)
    with open(out_filename, 'w', encoding='utf-8') as file:
        file.write(short_line)
    print(f"\n Строка наименьшей длины записана в файл '{out_filename}':")
    print(short_line)
else:
    print("Файл пуст или не содержит строк.")