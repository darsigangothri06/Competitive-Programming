date = "6th Nov 1960"
Date = ''
L = date.split()
Date += L[-1]
Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
ind = Month.index(L[1])
if ind < 9:
    Date += '-0' + str(ind+1)
else:
    Date += '-' + str(ind+1)
if len(L[0]) == 3:
    Date += '-0' + L[0][0]
else:
    Date += '-' + L[0][:2]
print(Date)
