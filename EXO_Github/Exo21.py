def length(lst):
    return len(lst)

def mean(lst):
    if len(lst) == 0:
        return None
    return sum(lst) / len(lst)

def range_of_list(lst):
    if len(lst) == 0:
        return None
    return max(lst) - min(lst)

def median(lst):
    if len(lst) == 0:
        return None
    sorted_list = sorted(lst)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    return sorted_list[mid]

def standard_deviation(lst):
    if len(lst) == 0:
        return None
    avg = mean(lst)
    variance = sum((x - avg) ** 2 for x in lst) / len(lst)
    return variance ** 0.5

def list_statistics(lst):
    return {
        "Length": length(lst),
        "Mean": mean(lst),
        "Range": range_of_list(lst),
        "Median": median(lst),
        "Standard Deviation": standard_deviation(lst),
    }

numbers = [1, 2, 3, 4, 5]
print("Numbers:", numbers)
print("Length:", length(numbers))
print("Mean:", mean(numbers))
print("Range:", range_of_list(numbers))
print("Median:", median(numbers))
print("Standard Deviation:", standard_deviation(numbers))
print("List Statistics:", list_statistics(numbers))

empty_list = []
print("\nEmpty List:", empty_list)
print("List Statistics:", list_statistics(empty_list))

single_element_list = [10]
print("\nSingle Element List:", single_element_list)
print("List Statistics:", list_statistics(single_element_list))

negative_numbers = [-5, -2, -3, -10]
print("\nNegative Numbers List:", negative_numbers)
print("List Statistics:", list_statistics(negative_numbers))

floating_numbers = [1.5, 2.7, 3.8, 4.1, 5.6]
print("\nFloating Point Numbers List:", floating_numbers)
print("List Statistics:", list_statistics(floating_numbers))
