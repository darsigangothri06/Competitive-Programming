L = input("Enter a sentence: ").split()
D = {}  # word-rank pairs
Str = ''  # for required sentence
for i in L:
    A = {i[:len(i)-1]:int(i[len(i)-1])} # taking key as word and number as value
    D.update(A)
keys = list(D.keys())  # taking all keys into a list
values = list(D.values())  # taking all values into another list
for i in sorted(values):  # sorting the values into i
    ind = values.index(i)  # i contains sorted values --- finding index of i in values list
    Str += keys[ind]  # getting the key for value i and adding to string
    Str += ' '  # adding space after every word
print(Str)
