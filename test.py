from quicksort import quicksort

def test():
    
    arr = [5,3,2]
    quicksort(0,2,arr)
    assert(arr == [2,3,5])

    arr = [2,2,1]
    quicksort(0,2,arr)
    assert(arr == [1,2,2])

    arr = [8,3,1,2,4]
    quicksort(0,4,arr)
    assert(arr == [1,2,3,4,8])

    arr = [1]
    quicksort(0,0,arr)
    assert(arr == [1])

    print("All Tests Passed!")


if __name__ == "__main__":
    test()