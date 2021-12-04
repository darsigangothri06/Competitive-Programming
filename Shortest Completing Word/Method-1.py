licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]
Main = ''
for i in licensePlate:
    if i.isalpha():
        Main += i.lower()
print(Main)
for i in words:
    if sorted(Main) == sorted(i):
        print(i)
        break
