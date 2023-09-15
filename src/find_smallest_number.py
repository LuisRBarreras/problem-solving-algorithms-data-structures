def find_smallest_number_log_linear(list_numbers):
    print("Before sort: {0}".format(list_numbers))
    list_numbers.sort()
    print("After sort: {0}".format(list_numbers))
    return list_numbers[0] if len(list_numbers) > 0 else 0


def find_smallest_number_linear(list_numbers):
    smallest_number = None
    for number in list_numbers:
        print("current smallest_number: {0}".format(smallest_number))
        if smallest_number == None or number < smallest_number:
            smallest_number = number

    return smallest_number


if __name__ == "__main__":
    # case1 = find_smallest_number_log_linear([3, 1, 8, 9])
    # assert case1 == 1

    # case2 = find_smallest_number_log_linear([])
    # assert case2 == 0

    case1 = find_smallest_number_linear(
        [
            3,
            1,
            8,
            9,
        ]
    )
    assert case1 == 1
