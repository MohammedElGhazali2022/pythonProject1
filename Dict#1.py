keys = ['Ten', 'Twenty', 'Thirsty']
values = [10, 20, 30]

dictionary = {}
for a in range(len(keys)):
    dictionary.update({keys[a]: values[a]})
print(dictionary)