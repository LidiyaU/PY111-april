# from typing import Sequence, TypeVar
#
#
# _Tt = TypeVar("T")

import random


# def sort(container: Sequence[_Tt]) -> Sequence[_Tt]:
def sort(container):
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) <= 1:
        return container
    else:
        sup_elem = random.choice(container)
        left_cont = [elem for elem in container if elem < sup_elem]

        # list.count(elem) проверяет, сколько раз элемент встречается в массиве
        mid = [sup_elem] * container.count(sup_elem)

        right_cont = [elem for elem in container if elem > sup_elem]
        return sort(left_cont) + mid + sort(right_cont)


#print(sort([5,1,3,7,2,4]))
