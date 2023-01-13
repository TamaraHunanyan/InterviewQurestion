
def invertArray(arr):
    halfLength = len(arr) // 2
    for idx in range(halfLength):
        arr[idx], arr[-idx - 1] = arr[-idx - 1], arr[idx]

def run():
    arr = ['p', 'y', 't', 'h', 'o', 'n']
    print("Before", arr)
    invertArray(arr)
    print("After", arr)
