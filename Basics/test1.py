
def checkMagazine(magazine, note):
    temp = list(set(note))
    for t in temp:
        if not note.count(t) <= magazine.count(t):
            print('No')
            exit(0)
        # else:
        #     magazine.remove(magazine[magazine.index(t)])
    print('Yes')

if __name__ == '__main__':

    magazine = input().rstrip().split()
    note = input().rstrip().split()
    checkMagazine(magazine, note)
