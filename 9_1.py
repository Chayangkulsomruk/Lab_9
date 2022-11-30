def linear_search(Data, n, UserInput):

    for i in range(0, n):

        if (Data[i] == UserInput):
            return i

    return -1

def linear_UserInput(Data, n, UserInput1):

    for i in range(0, n):

        if (Data[i] == UserInput1):
            return i

    return -1



Data = [7, 10, 12, 14, 1, 20, 29, 37]
UserInput = 14
UserInput1 = 29

n = len(Data)
func1 = linear_search(Data, n, UserInput)
func2 = linear_UserInput(Data, n, UserInput1)

print("Answer of 14 is:", func1)
print("Answer of 29 is:", func2)