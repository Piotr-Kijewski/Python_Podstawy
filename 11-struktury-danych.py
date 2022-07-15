# names_list = []  # tworzymy pustą listę
# names_list.append('Kamil')  # dodanie danych do listy --> .append()
# names_list.append('Mariusz')

# print(names_list)

# names_list = ['Kamil', 'Mariusz', 'Adam']
# # print(names_list)

# # for name in names_list:  # dla każdego imienia z listy wykonaj jakąś rzecz
# #     print(name)

# # names_list.reverse() # odwrócenie kolejności listy

# # for name in names_list:
# #     print(name)

# names_list.sort() # sortowanie
# print(names_list)
# names_list.sort(reverse=True) # sortowanie w odwrotną stronę
# print(names_list)

# for name in names_list:
#     print(name)

# names_list = ['Kamil', 'Mariusz', 'Adam']
# print(names_list[0]) # wyświetlanie po argumencie

# # names_list = ['Kamil', 'Mariusz', 'Adam', 'Kamil']
# # print(names_list.count('Kamil')) # sprawdzamy ile razy występuje 'Kamil'  w liście

# # print(len(names_list)) # sprawdzamy ile jest pozycji w liście

# # # metoda .pop zwraca argument i usuwa go z listy
# # names_list = ['Kamil', 'Mariusz', 'Adam', 'Kamil']
# # print(names_list)
# # print()
# # print(names_list.pop(0))
# # print()
# # print(names_list)

# # # metoda .remove usuwa pierwsze wystąpienie z listy
# # names_list = ['Kamil', 'Mariusz', 'Adam', 'Kamil']
# # names_list.remove('Kamil')
# # print(names_list)

# # # metoda .clear usuwa wszystko z listy
# # names_list = ['Kamil', 'Mariusz', 'Adam', 'Kamil']
# # names_list.clear()
# # print(names_list)

# # # łączenie list
# # names_list = ['Kamil', 'Mariusz', 'Adam', 'Kamil']
# # names_list_2 = ['Dominik']
# # names_list_3 = names_list + names_list_2
# # print(names_list_3)

# # krotka - struktura niezmienna
# # person = ('Jan', 'Nowak', 30)
# # print(len(person))

# # print(person)

# # set - podobnie jak lista, ale nie może być zduplikowanych danych, elementy są nie butowalne, nie są uporządkowane
# names_set = {'Kamil', 'Mariusz', 'Kamil'}
# print(names_set)

# names_set_2 = set() # tworzymy pusty set

# names_set_2.add('Kamil') # metodą .add dodajemy do set-a
# names_set_2.add('Dominik')
# print(names_set_2)

# names_set_2.remove('Kamil') # usuwamy 'Kamil' z set-a
# names_set_2.discard('Dominik')
# print(names_set_2)

# # wyświetlanie dwóch set-ów metodą .union
# names_set_3 = {'Mariusz', 'Tytus'}
# names_set_4 = names_set.union(names_set_3)
# for name in names_set_4:
#     print(name)
# print(names_set_4)

# # łączenie dwóch setów metodą .update
# names_set.update(names_set_3)
# print(names_set)

# porównywanie dwóch zbiorów
# names_set_5 = {'Kamil', 'Dominik'}
# names_set_6 = {'Mariusz', 'Tytus', 'Kamil'}
# names_set_7 = names_set_5.difference(names_set_6) # jesli jest coś wspólnego w zbiorach, to usuwane zostaje z pierwszego zbioru
# for name in names_set_7:
#     print(name)
    
# names_set_7 = names_set_5.intersection(names_set_6) # jesli jest coś wspólnego w zbiorach, to zostanie to wyświetlone
# for name in names_set_7:
#     print(name)
    
# names_set_7 = names_set_5.symmetric_difference(names_set_6) # jesli jest coś wspólnego w zbiorach, to zostanie to pominięte
# for name in names_set_7:
#     print(name)
    
# wyczyszczenie set-u
# names_set_5.clear()
# for name in names_set_5:
#     print(name)

# dodawanie do listy set-a
# names_list = ['Artur', 'Rafał']
# names_set = {'Mariusz', 'Tytus', 'Kamil'}

# names_list.extend(names_set) # metoda .extend pozwala dodać set-a do listy
# print(names_list)


# Dictionary - słownik

# countries_and_capitals = {'Poland': 'Warsaw', 'Germany': 'Berlin'}
# countries_and_capitals['Czechia'] = 'Prague'

# print(countries_and_capitals)

# for country in countries_and_capitals.keys(): # wyświtlamy po kluczu
#     print(country)
    
# for capitals in countries_and_capitals.values(): # wyświtlamy po wartości
#     print(capitals)

# for country, capitals in countries_and_capitals.items(): # wyświtlamy wszystko
#     print(country + '-' + capitals)

# dwie metody pozwalające wyszukać po konkretnym kluczu    
# print(countries_and_capitals['Poland'])
# print(countries_and_capitals.get('Poland'))

# print('Podaj nazwę państwa, np. Poland, Germany, Czechia:')
# country = input()
# print(countries_and_capitals.get(country))

# dodanie kolejnego klucza jeśli wczesniej go tam nie było, państwo + stolica za pomocą metody .setdefault
# print(countries_and_capitals.setdefault('USA', 'Washington DC'))
# print(countries_and_capitals)

# print(countries_and_capitals.popitem()) # usuwamy ostatnio dodany klucz
# print(countries_and_capitals)

