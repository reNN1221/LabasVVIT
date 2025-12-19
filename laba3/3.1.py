from fileinput import close

with open('example.txt') as file:
    content = file.read()
    close()

def read_file(filename, mode):
    try:
        if mode == 'lines':
            with open(filename) as file:
                for line in file:
                    return line
        elif mode == 'all':
            with open(filename) as file:
                return file.read()
        else:
            print("Неверно введены данные")
            return None
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return None


print('1. Построчно')
print('2. Чтение всего файла')

try:
    num = int(input('Выберите способ открытия: '))
    if num == 1:
        data = read_file('example.txt', mode='lines')
        if data:
            print("\nСодержимое файла:")
            for line in data:
                print(line)
    elif num == 2:
        data = read_file('example.txt', mode='all')
        if data:
            print("\nСодержимое файла:")
            print(data)
    else:
        print('Введите 1 или 2')

except ValueError:
    print('Введите корректное числовое значение')