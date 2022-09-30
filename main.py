numbers = [12,75,150,180,145,525,50]
import math

for num in numbers:
    if num % 5 == 0:
        number = num
        if number > 500 :
            break
        elif number > 150 :
            continue
        print(number)