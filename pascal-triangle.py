#leetcode link: https://leetcode.com/problems/pascals-triangle/


def nPascal(n):
    pascalForN = [1]
    ans =1
    for i in range(1, n):
        ans = ans * (n - i)
        ans = ans / i
        pascalForN.append(int(ans))
    return pascalForN


def generate(numRows):
    finalPascal = []
    for i in range(1,numRows+1):
        finalPascal.append(nPascal(i))

    return finalPascal
        

numOfRows = 5

print(generate(numOfRows))