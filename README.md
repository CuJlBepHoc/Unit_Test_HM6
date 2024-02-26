# Урок 6. Юнит тестирование в других языках

## Задание 1. Создайте программу на Python или Java, которая принимает два списка чисел и выполняет следующие действия:

a. Рассчитывает среднее значение каждого списка.

b. Сравнивает эти средние значения и выводит соответствующее сообщение:

- "Первый список имеет большее среднее значение", если среднее значение первого списка больше.

- "Второй список имеет большее среднее значение", если среднее значение второго списка больше.

- "Средние значения равны", если средние значения списков равны.

**Важно:**

- Приложение должно быть написано в соответствии с принципами объектно-ориентированного программирования.

- Используйте Pytest (для Python) или JUnit (для Java) для написания тестов, которые проверяют правильность работы программы. Тесты должны учитывать различные сценарии использования вашего приложения.

- Используйте pylint (для Python) или Checkstyle (для Java) для проверки качества кода.

- Сгенерируйте отчет о покрытии кода тестами. Ваша цель - достичь минимум 90% покрытия.

**Формат и требования к сдаче:**

Отчет о выполнении этого задания должен включать в себя следующие элементы:

- Код программы

- Код тестов

- Отчет pylint/Checkstyle

- Отчет о покрытии тестами

- Объяснение того, какие сценарии покрыты тестами и почему вы выбрали именно эти сценарии.
---

## Реализация

- Отчет о качестве кода (SonarLint)

![Отчет о качестве кода]([add_files/SonarLint Report.png](https://github.com/CuJlBepHoc/Unit_Test_HM6/blob/main/add_files/SonarLint%20Report.png))

- Отчет о покрытии тестами

![Отчет о покрытии тестами]([add_files/Coverage report 1.png](https://github.com/CuJlBepHoc/Unit_Test_HM6/blob/main/add_files/Coverage%20report%201.png))

## Сценарии, покрытые тестами

1. **test_right_list_empty**: Проверка сценария, когда правый список пуст, а левый список содержит элементы.
2. **test_left_list_empty**: Проверка сценария, когда левый список пуст, а правый список содержит элементы.
3. **test_both_lists_empty**: Проверка сценария, когда оба списка пусты.
4. **test_different_averages**: Проверка сценария, когда средние значения двух списков различны.
5. **test_equal_averages**: Проверка сценария, когда средние значения двух списков равны.
6. **test_both_lists_contain_one_element**: Проверка сценария, когда оба списка содержат по одному элементу.
7. **test_both_lists_contain_many_elements**: Проверка сценария, когда оба списка содержат много элементов.
8. **test_both_lists_contain_negative_numbers**: Проверка сценария, когда оба списка содержат отрицательные числа.
9. **test_both_lists_contain_float_numbers**: Проверка сценария, когда оба списка содержат числа с плавающей запятой.
10. **test_one_list_invalid_input**: Проверка сценария, когда передается недопустимый тип данных в один из списков.
11. **test_lists_have_different_lengths**: Проверка сценария, когда списки имеют разную длину.

### Пояснение к выбранным тестам:

- **Пустые списки**: Тесты с пустыми списками важны для корректной работы кода при пустых входных данных.
- **Средние значения**: Проверка различных средних значений гарантирует корректность сравнения средних значений списков.
- **Разные длины списков**: Тесты с разной длиной списков важны для обработки случаев, когда входные данные различаются по объему.
- **Разнообразие значений**: Тесты с различными типами значений обеспечивают обработку разнообразных входных данных.
- **Недопустимый ввод**: Тест на недопустимый ввод важен для обработки ошибочных ситуаций при передаче неверных данных.
