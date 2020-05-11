"""
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Input: haystack = "hello", needle = "ll"  /  Output: 2

Input: haystack = "aaaaa", needle = "bba"  /  Output: -1
Input: haystack = "mississippi", needle= "issip"  /  Output: 4
"""

class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        if needle in haystack:
            n_index = h_index = 0
            rIndex = -1
            match = False

            while h_index < len(haystack):
                while n_index < len(needle):
                    if needle[n_index] == haystack[h_index]:
                        if match == False:
                            rIndex = h_index
                        print("rIndex is:- {}".format(rIndex))
                        n_index += 1
                        h_index += 1
                        match = True
                    else:
                        if match == True:
                            h_index = rIndex
                        match = False
                        n_index = 0
                        h_index += 1
                        rIndex = -1
                    print("needle at={} - haystack at={}".format(n_index, h_index))
                return rIndex
        else:
            return -1

if __name__ == '__main__':
    s = Solution()
    haystack = "mississippi"
    needle= "issip"
    print(s.strStr(haystack, needle))

