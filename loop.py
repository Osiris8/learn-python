numbers = [1, 2, 3 , 4, 5, 6, 7, 8]

for number in numbers:
    if (number > 0):
        print("number bigger than 0 detected")
        break
    print(number)
    
for number in numbers:
    print(number)

hungry = True
while hungry:
  print("Time to eat!")
hungry = False