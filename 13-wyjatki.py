countries_and_capitals = {'Poland': 'Warsaw',
                          'Czechia': 'Prague', 'Germany': 'Berlin'}

try:
    print(2 / 2)
    print(countries_and_capitals['USA'])
except KeyError: # KeyError - klucz wyjątku
    print('Klucz nie został znaleziony!')
except ZeroDivisionError:
    print('Nie można dzielić przez 0')
finally:
    print('To wykona się zawsze')

print('Jestem tutaj')
