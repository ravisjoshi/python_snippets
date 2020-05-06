"""
The first line contains an integer n, the number of socks represented in ar.
The second line contains n space-separated integers describing the colors ar[i] of the socks in the pile.
n = 9
ar = '10 20 30 10 60 20 30 50 10'
Output: 3
"""
#!/bin/python3

def sockMerchant(n, ar):
    socksDict = {}
    result = 0
    for num in range(n):
        if ar[num] not in socksDict.keys():
            socksDict.update({ar[num]: 1})
        else:
            value = socksDict.get(ar[num]) + 1
            if value % 2 == 0:
                result += 1
            socksDict.update({ar[num]: value})

    return result

if __name__ == '__main__':

    n = int(input('How many numbers you want to enter:-  '))
    ar = list(map(int, input('Enter a space seperated number list:-  ').rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
