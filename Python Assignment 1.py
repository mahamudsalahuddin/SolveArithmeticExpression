# Write a python script to take a mathematical expression as input that may contains '+', '-', '/', '*', and '()'. Display the output after solving the expression.
# ** Don't use eval() function
#
# Input:
# 7+8+(10-5)*20/4
# Output:
# 40
#solution:
# it work without bracket

def evaluate(string):
    # string = string.replace(" ", "")
    #1+2x3-4/5

    def splitby(string, separators):

        lis = []
        current = ""
        for ch in string:
            if ch in separators:
                lis.append(current)
                lis.append(ch)
                current = ""
            else:
                current += ch
        lis.append(current)
        # print(lis)
        return lis

    lis = splitby(string, "+-")

    def multiAndDiv(string):
        lis = splitby(string, "x/")
        # print(lis)
        if len(lis) == 1:
            return lis[0]

        output = float(lis[0])
        lis = lis[1:]

        while len(lis) > 0:
            operator = lis[0]
            number = float(lis[1])
            lis = lis[2:]

            if operator == "x":
                output *= number

            elif operator == "/":
                output /= number
        return output

    for i in range(len(lis)):
        lis[i] = multiAndDiv(lis[i])
        print(lis)

    output = float(lis[0])
    lis = lis[1:]

    while len(lis) > 0:
        operator = lis[0]
        number = float(lis[1])
        lis = lis[2:]

        if operator == "+":
            output += number
        elif operator == "-":
            output -= number
    return output

value = input("Enter the expression: ")
# value= "1+2x3-4/5"
print("The result is: ",evaluate(value))
