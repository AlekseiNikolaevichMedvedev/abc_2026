#todo: Дан массив размера N. Найти минимальное растояние между 
# одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !
# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]


# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

from __future__ import annotationsf
from typing import Any

def get_indices(input_list: list[Any]) -> dict[Any, list[int]]:
    output_dict = {}
    if input_list:
        for index, instance in enumerate(input_list):
            if instance not in output_dict:
                output_dict[instance] = []
            output_dict[instance].append(index)
    return output_dict

def prune_dict(input_dict: dict[Any, list[int]]) -> dict[Any, list[int]]:
    output_dict = {}
    if input_dict:
        for key, indices in input_dict.items():
            if len(indices) > 1:
                output_dict[key] = indices
    return output_dict

def find_min_distances(pruned_dict: dict[Any, list[int]]) -> dict[Any, list[int]]:
    output_dict = {}
    if pruned_dict:
        for key, indices in pruned_dict.items():
            min_dist = float('inf')
            min_indices = set()            
            for i in range(len(indices)-1):
                dist = indices[i+1] - indices[i]
                if dist < min_dist:
                    min_dist = dist
                    min_indices = {indices[i], indices[i+1]}
                elif dist == min_dist:
                    min_indices = min_indices | {indices[i], indices[i+1]}
            output_dict[key] = sorted(list(min_indices))
            
    return output_dict

if __name__ == "__main__":
    try: 
        raw_input = input("Введите числа через пробел или запятую: ").strip()
        clean_input = raw_input.replace(',',' ').split()
        mass = [int(x) for x in clean_input]
        indices = get_indices(mass)
        pruned = prune_dict(indices)
        result = find_min_distances(pruned)
        print("Результат:")
        print(result)
    except ValueError:
        print("Ошибка! Нужно вводить только целые числа через пробел или запятую.")



