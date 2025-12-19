import fileinput
text = input('Введите текст: ')

def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)
    return 'Текст записан в файл'

def app_list(filename, text):
    with open(filename, 'w') as file:
        file.write(text)
    return 'Текст добавлен в файл+'

text = input('Введите текст: ')
result = write_to_file('exapmle2.txt', text)
print(result)

text = input('Введите текст: ')
result = app_list('User_text', text)
print(result)
fileinput.close()
