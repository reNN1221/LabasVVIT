def read_file(filename):
    try:
        with open(filename) as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print('ERROR: Файл не найден')

content = read_file('example.txt')
print(content)
