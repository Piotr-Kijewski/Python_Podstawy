# 1. Przykład pierwszy

# countries_information = {} # tworzymy tablicę
# countries_information['Polska'] = ('Warszawa', 37.97) # dodajemy wartości [klucz] (wartość)
# countries_information['Niemcy'] = ('Berlin', 83.02)
# countries_information['Słowacja'] = ('Bratysława', 5.45)

# def show_country_info(country): # zdefiniowana (stworzona) została funkcja show_country_info
#     country_information = countries_information.get(country) # zmienna która zawiera wartośc dla danego klucza, np Polska --> ('Warszawa", 37.97) 

#     print()
#     print(country)
#     print('------------')
#     print('Stolica: ' + country_information[0])
#     print('Liczba mieszkańców (mln): ' + str(country_information[1])) # mozna zrobić tak: print('Liczba mieszkańców (mln): ', country_information[1])
    

# for country in countries_information.keys(): # pętla - przypisujemy zmienną country do klucza (państwo)
#     print(country) # wyświetlamy państwo z tablicy (klucze)

# country = input('Informacje o jakim kraju chcesz wyświetlić?') # wpisujemy z konsoli kraj (klucz) który zostanie przypisany do zmiennej country

# show_country_info(country) # wywołanie stworzonej wcześniej funkcji ale z kluczem podanym przez nas


# 2. Przykład drugi

def display_sum_1(a, b):
    print(a+b) # zwraca odrazu wartość

def calculate_sum_2(a, b):
    return a + b # nie zwraca wartości

def print_message():
    print('To jest super wiadomość!')
      
display_sum_1(2, 3) # uruchamia funkcję pierwszą

sum = calculate_sum_2(5, 3) # uruchamia funkcję drugą
print(sum) # zwraca wartość z funkcji ddrugiej

print_message() # uruchamia funkcję trzecią