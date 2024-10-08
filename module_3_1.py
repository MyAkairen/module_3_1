calls = 0

def count_calls():                          # счетчик вызова функций
    global calls
    calls = calls + 1

def string_info(string):                    # преобразование строки
    count_calls()
    return (len(string), string.upper(),string.lower())


def is_contains(string,list_to_search):     # проверка на содержимое
    count_calls()
    for i in range(len(list_to_search)):
        if string.lower() == list_to_search[i].lower():
            return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
