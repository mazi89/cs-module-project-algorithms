'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    dic = {}
    for i in arr:
        dic[i] = 1 if dic.get(i) is None else dic[i] + 1
    print(dic)
    for k, v in dic.items():
        if v < 2:
            return k

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")