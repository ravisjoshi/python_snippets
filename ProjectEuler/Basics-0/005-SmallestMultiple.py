"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def smallest_nultiple(num):
    if num == 1 or num == 2:
        return num
    result = 2
    output = [2]
    for index in range(3, num+1):
        temp = index
        for n in output:
            if temp % n == 0 and temp > 1:
                temp = temp // n
            elif temp == 1:
                break
        if not result % index == 0 and index == temp:
            result = result * index
            output.append(index)
        else:
            result = result * temp
            output.append(temp)

    return result

num = 20
print(smallest_nultiple(num))
