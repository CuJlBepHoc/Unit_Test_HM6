from Average_comparator import AverageComparator

if __name__ == "__main__":
    list1 = [int(x) for x in input("Введите числа первого списка через пробел: ").split()]
    list2 = [int(x) for x in input("Введите числа второго списка через пробел: ").split()]

    comparator = AverageComparator(list1, list2)
    result = comparator.compare_averages()
    print(result)
