def Tour(Mat,cnt=1,Adv=0,Pl=0):
    Pl = Mat//2
    Adv = Mat - Pl
    if Adv == 1:
        return cnt
    else:
        cnt += Pl
        return Tour(Adv,cnt)
Num = int(input("Enter number of teams: "))
print(Tour(Num))