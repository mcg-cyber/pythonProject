def mylist(numbers: list):

    test_list = []
    for nums in numbers:
        if nums % 2 == 0:
            test_list.append(nums)

    return test_list


print(mylist([1, 2, 3, 4, 8, 13, 12]))
