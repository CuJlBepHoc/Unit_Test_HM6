class AverageComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, lst):
        if not lst:
            return None
        return sum(lst) / len(lst)

    def compare_averages(self):
        avg1 = self.calculate_average(self.list1)
        avg2 = self.calculate_average(self.list2)

        if avg1 is None and avg2 is None:
            return "Оба списка пусты"
        elif avg1 is None:
            return "Первый список пуст"
        elif avg2 is None:
            return "Второй список пуст"

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        elif avg2 > avg1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
