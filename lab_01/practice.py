## Task 1
def is_even(num):
    return not num % 2


# print([i for i in range(1, 10) if (is_even(i))])

## Task 2
my_dictionary = {"First name": "Bence", "Second Name": "Háromi"}

# print(my_dictionary)

# for item in my_dictionary.items():
#    print(item)

## Task 3


def is_first_and_last_same(list):
    return list[0] == list[-1]


num_list = [10, 5, 6, 10]
# print(is_first_and_last_same(num_list))

## Task 4
def sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum


def mean(list):
    return sum(list) / len(list)


def power(base, power):
    if power == 0:
        return 1
    result = 1
    for i in range(1, power + 1):
        result *= base
    return result


def variance(list):
    return sum([power(i - mean(list), 2) for i in list]) / len(list)


nums = [1, 3, 3, 6, 3, 2, 7, 5, 9, 1]

# print(variance(nums))

## Task 5
def factorial(integer):
    if integer == 0:
        return 1
    result = 1
    for i in range(integer):
        result *= integer - i
    return result


# print(factorial(100))