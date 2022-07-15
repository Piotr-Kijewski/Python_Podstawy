# number = 1

# while number < 6:
#     print(number)
#     number += 1
    
# for number in range(0, 11, 2): # w nawiasie (0, 11, 2) zakres od 0 do 10 z krokiem co 2!
#     print(number)
    
for number in range(0, 10):
    if number == 5:
        break   # przerwanie pętli
    print(number)

for number in range(0, 10):
    if number == 5:
        continue   # pominięcie pozycji w pętli
    print(number)