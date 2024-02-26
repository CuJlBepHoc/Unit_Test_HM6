import pytest
from Average_comparator import AverageComparator


def test_right_list_empty():
    comparator = AverageComparator([1, 2, 3], [])
    assert comparator.compare_averages() == "Второй список пуст"

def test_left_list_empty():
    comparator = AverageComparator([], [1, 2, 3])
    assert comparator.compare_averages() == "Первый список пуст"

def test_both_lists_empty():
    comparator = AverageComparator([], [])
    assert comparator.compare_averages() == "Оба списка пусты"

def test_different_averages():
    comparator = AverageComparator([1, 2, 3], [4, 5, 6])
    assert comparator.compare_averages() == "Второй список имеет большее среднее значение"

def test_equal_averages():
    comparator = AverageComparator([1, 2, 3], [3, 1, 2])
    assert comparator.compare_averages() == "Средние значения равны"

def test_both_lists_contain_one_element():
    comparator = AverageComparator([5], [3])
    assert comparator.compare_averages() == "Первый список имеет большее среднее значение"

def test_both_lists_contain_many_elements():
    comparator = AverageComparator([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
    assert comparator.compare_averages() == "Второй список имеет большее среднее значение"

def test_both_lists_contain_negative_numbers():
    comparator = AverageComparator([-1, -2, -3], [-4, -5, -6])
    assert comparator.compare_averages() == "Первый список имеет большее среднее значение"

def test_both_lists_contain_float_numbers():
    comparator = AverageComparator([1.5, 2.5, 3.5], [4.5, 5.5, 6.5])
    assert comparator.compare_averages() == "Второй список имеет большее среднее значение"

def test_one_list_invalid_input():
    with pytest.raises(TypeError):
        comparator = AverageComparator([1, 2, 3], "invalid_input")
        comparator.compare_averages()

def test_lists_have_different_lengths():
    comparator = AverageComparator([1, 2, 3], [1, 2, 2, 3])
    assert comparator.compare_averages() == "Средние значения равны"