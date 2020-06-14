"""
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.
Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows.
Please note that both secret number and friend's guess may contain duplicate digits.

Input: secret = "1807", guess = "7810"  /  Output: "1A3B"
Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

Input: secret = "1123", guess = "0111"  /  Output: "1A1B"
Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.

Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
"""

class Solution:
    def getHint(self, secret, guess):
        bull, cow = 0, 0
        s_secret = sorted(secret)

        for index, value in enumerate(guess):
            if guess[index] == secret[index]:
                bull += 1
            if value in s_secret:
                cow += 1
                s_secret.remove(value)

        return str(bull)+'A'+str(cow-bull)+'B'


s = Solution()

secret = "1807"
_guess = "7810"
print(s.getHint(secret, _guess))

secret = "1123"
_guess = "0111"
print(s.getHint(secret, _guess))

secret = "011"
_guess = "110"
print(s.getHint(secret, _guess))
