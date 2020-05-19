# Enter your code here. Read input from STDIN. Print output to STDOUT

ad, am, ay = input().split()
ed, em, ey = input().split()

result = 0
if int(ay) != int(ey):
    if int(ay) > int(ey):
        result = 10000
    else:
        result = 0
elif int(am) != int(em):
    if int(am) > int(em):
        result = 500*(int(am)-int(em))
    else:
        result = 0
elif int(ad) != int(ed):
    if int(ad) > int(ed):
        result = 15*(int(ad)-int(ed))
    else:
        result = 0

if result >= 0:
    print(result)
else:
    print('0')

"""
2 6 2014
5 7 2014

31 12 2009
1 1 2010
"""