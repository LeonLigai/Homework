from re import findall

file_path = 'MOCK_DATA.txt'
pochta = 'pochta.txt'
fio = 'fio.txt'
rashirenie = 'rashirenie.txt'
cvet = 'cvet.txt'

init_read = open(file_path, mode='r', encoding='UTF-8')

pochta_file = open(pochta, mode='w', encoding='UTF-8')
fio_file = open(fio, mode='w', encoding='UTF-8')
rashirenie_file = open(rashirenie, mode='w', encoding='UTF-8')
cvet_file = open(cvet, mode='w', encoding='UTF-8')
txt_file = init_read.read()

pochta_file_search = r'[\w_-]+@[\w_-]+.[\w.]+'
pochta_result = findall(pochta_file_search, txt_file)
fio_file_search = r"[A-Z][a-z_-]+[\s][de\sA-Z'\s]+[a-zA-Z]+"
fio_result = findall(fio_file_search, txt_file)
rashirenie_file_search = r'[A-Z\s]+[a-zA-Z]+[.][a-z\d]+'
rashirenie_result = findall(rashirenie_file_search, txt_file)
cvet_file_search = r'#......'
cvet_result = findall(cvet_file_search, txt_file)

for email in pochta_result:
    print(email)
    pochta_file.write(email + '\n')

for name in fio_result:
    print(name)
    fio_file.write(name + '\n')

for exp in rashirenie_result:
    print(exp)
    rashirenie_file.write(exp + '\n')

for font in cvet_result:
    print(font)
    cvet_file.write(font + '\n')


print(f'Total results of file: {str(len(pochta_result))}\n')
print(f'Total results of file: {str(len(fio_result))}\n')
print(f'Total results of file: {str(len(rashirenie_result))}\n')
print(f'Total results of file: {str(len(cvet_result))}\n')