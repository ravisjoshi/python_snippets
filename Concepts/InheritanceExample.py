"""
Grade:
O  90 <= a <= 100
E  80 <= a <= 90
A  70 <= a <= 80
P  55 <= a <= 70
D  40 <= a <= 55
T  a < 40

Input:-
Heraldo Memelli 8135627 <- fName, lName & id
2       <- number of subjects
100 80  <- arrary of numbers in different subjects

Output:-
Name: Memelli, Heraldo
ID: 8135627
Grade: O
"""

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    """
    Parameters:
    firstName - A string denoting the Person's first name.
    lastName - A string denoting the Person's last name.
    id - An integer denoting the Person's ID number.
    scores - An array of integers denoting the Person's test scores.
    Write your constructor here
    """
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

        def calculate(self):
            iAvg = sum(self.scores) / len(self.scores)
            return 'O' if iAvg > 89 else 'E' if iAvg > 79 else 'A' if iAvg > 69 else 'P' if iAvg > 54 else 'D' if iAvg > 39 else 'T'
    """
    Function Name: calculate
    Return: A character denoting the grade.
    Write your function here
    """
    def calculate(self):
        iAvg = sum(self.scores)//len(self.scores)
        return 'O' if iAvg > 89 else 'E' if iAvg > 79 else 'A' if iAvg > 69 else 'P' if iAvg > 54 else 'D' if iAvg > 39 else 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
