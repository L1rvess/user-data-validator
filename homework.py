import fnmatch
info = input('Введите данные которые вас просят! чтобы продолжить нажмите Enter: ')
name = input('enter your name: ')
while name.isalpha() == False:
    name = input('enter your name: ')

surname = input('enter ur surname: ')
while surname.isalpha() == False:
    surname = input('enter ur surname: ')

date_of_birthday = input('enter your birthday: ')
while fnmatch.fnmatch(date_of_birthday, '??.??.????') == False:
    print('дата рождения должна соответствовать шаблону 01.01.2000!')
    date_of_birthday = input('enter your birthday: ')

year = 2025 - int(date_of_birthday[-4:])  # например, 2025 - 2000 = 25
age = input('enter your age: ')
while not age.isdigit() or int(age) != year:
    print(f'По дате рождения вам должно быть {year} лет. Попробуйте снова.')
    age = input('enter your age: ')

mail = input('enter ur mail: ')
while fnmatch.fnmatch(mail, '*?@*?.*?') == False:
    print('почта должна соответствовать шаблону dog@mail.com!!!!!!')
    mail = input('Введите свою почту: ')

print(
    f' Ваше имя: {name}\n'
    f' Ваша фамилия: {surname}\n'
    f' Ваш возраст: {age}\n'
    f' Ваша дата рождения: {date_of_birthday}\n'
    f' Ваша почта: {mail}\n'
)