# name = 'kamil'
# name_2 = 'MAŁY'

# print(len(name)) # sprawdzamy ile znaków znajduje się w zmiennej

# print(name.capitalize()) # metoda (bez argumentów) zamienia pierwszą literę na wielką literę

# print(name.upper()) # metoda (bez argumentów) zamienia wszystkie litery na wielkie

# print(name_2.lower()) # metoda (bez argumentów) zamienia wszystkie litery na małe

# name = 'Kamil'

# print(name[0]) # metoda [] podaje wartość ze zmiennej po indeksie, zaczynamy od 0, 1, 2, 3...
# print(name[0:2])
# print(name[3:])
# print(name[-3:]) # podajemy od końca (ostatnie trzy litery)

# channel = 'Jak nauczyć się programowania'
# print(channel.split(' ')) # dzielimy na pojedyńcze słowa, jest tutaj argument np. spacja " "

# # łączenie poszczególnych stringów - metoda join
# join_string = ' '
# print(join_string.join(['Jak', 'nauczyć', 'się', 'programowania'])) # uwaga na kwadratowe nawiasy

# print(name.startswith('K')) # metoda sprawdzająca czy słowo zaczyna się na daną literę (uwaga na wielkość liter)
# print(name.startswith('k'))

# print(name.endswith('l')) # metoda sprawdzająca czy słowo kończy się na daną literę (uwaga na wielkość liter)
# print(name.endswith('k'))

# print(name.rstrip('l')) # metoda pozwalająca na usunięcie z prawej strony literę ze stringa

# print(name.lstrip('K')) # metoda pozwalająca na usunięcie z lewej strony literę ze stringa

# name_2 = 'aKamila'
# print(name_2.strip('a')) # metoda pozwalająca na usunięcie z lewej jak i prawej strony daną literę ze stringa

# name_3 = '   Kamil '
# print(name_3)
# print(name_3.strip()) # metoda pozwalająca na usunięcie np. nadmiarowych spacji z obu stron stringa

# first_name = 'Jan'
# last_name = 'Nowak'

# print(first_name + ' ' + last_name)
# print(first_name, last_name)

# join_string = ' '
# print(join_string.join([first_name, last_name]))

james_bond = 7
print(str(james_bond).zfill(3))