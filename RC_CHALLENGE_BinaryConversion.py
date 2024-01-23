# CONVERT A FLOAT TO A BINARY NUMBER
# 1/23/2024

def binFunc(decNum):
    # SEPARATE INTEGER AND DECIMAL VALUES
    intNum = int(decNum)
    frac = decNum - intNum
    print("The binary number for " + str(decNum) + " is:")

    # CONVERT INTEGER TO BINARY NUMBER
    intToBin(intNum)

    print(".", end = '')

    # CONVERT DECIMAL TO BINARY NUMBER
    decToBin(frac)

def intToBin(intNum):
    if intNum >= 1:
        intToBin(intNum // 2)
    print(intNum % 2, end = '') # end prints all nums on same line

def decToBin(frac):
    if frac > 0:
        decToBin((frac * 2) - int(frac * 2))
    print(int(frac * 2), end = '')

print("Enter a positive or negative number:")
try:
    x = float(input())
except ValueError:
    raise ValueError("Input could not be converted to a number.")
else:
    binFunc(abs(x))

