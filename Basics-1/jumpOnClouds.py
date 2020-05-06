"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Input: 0 0 1 0 0 1 0
Output: 4

Input: 0 0 0 0 1 0
Output: 3

Input: 0 0 0 1 0 0
Output: 3
"""
#!/bin/python3

def jumpingOnClouds(c):
    jumps = 0
    cloud = 0
    length = len(c)
    while cloud < length:
        if (cloud+2) < length and c[cloud+1] == 0 and c[cloud+2] != 0:
            cloud += 1
        elif (cloud+2) < length and c[cloud+1] != 0 and c[cloud+2] == 0:
            cloud += 2
        elif (cloud+2) < length and c[cloud+1] == 0 and c[cloud+2] == 0:
            cloud += 2
        elif (cloud+1) < length and c[cloud+1] == 0:
            cloud += 1
        else:
            break
        jumps += 1
        print("I am at {} with jump count {} - {}".format(cloud, jumps, len(c)))

    return jumps

if __name__ == '__main__':

    # c = list(map(int, input('Enter cloud details:- ').rstrip().split()))
    # c = [0, 0, 1, 0, 0, 1, 0]
    # c = [0, 0, 0, 0, 1, 0]
    c = [0, 0, 0, 1, 0, 0]

    print(jumpingOnClouds(c))
