def Binary_UserInput1(Data, l, r, UserInput1):
 
    if r >= l:
        mid = l + (r - l) // 2
        if Data[mid] == UserInput1:
            return mid
        elif Data[mid] > UserInput1:
            return Binary_UserInput1(Data, l, mid-1, UserInput1)
        else:
            return Binary_UserInput1(Data, mid + 1, r, UserInput1)
    else:
        return -1

def Binary_UserInput2(Data, l, r, UserInput1):
 
    if r >= l:
        mid = l + (r - l) // 2
        if Data[mid] == UserInput1:
            return mid
        elif Data[mid] > UserInput1:
            return Binary_UserInput2(Data, l, mid-1, UserInput2)
        else:
            return Binary_UserInput2(Data, mid + 1, r, UserInput2)
    else:
        return -1
 
 
Data = [7, 10, 12, 14, 1, 20, 29, 37]
UserInput1 = 14
UserInput2 = 29

ans1 = Binary_UserInput1(Data, 0, len(Data)-1, UserInput1)
ans2 = Binary_UserInput2(Data, 0, len(Data)-1, UserInput2)

print("Element 14 of index is% d" % ans1)
print("Element 14 of index is% d" % ans2)
