# from typing import Sequence, TypeVar
#
# _Tt = TypeVar("T")


def sort(container):
    """
        Sort input container with merge sort

        :param container: container of elements to be sorted
        :return: container sorted in ascending order
        """

    if len(container) <= 1:
        return container
    else:
        left_cont = container[:len(container) // 2]
        right_cont = container[len(container) // 2:]
        #        return merge_sort(left_cont,right_cont)
        return merge_sort(sort(left_cont), sort(right_cont))


def merge_sort(left_cont, right_cont):
    merged_cont = []
    i = 0
    j = 0

    while i < len(left_cont) and j < len(right_cont):
        if left_cont[i] <= right_cont[j]:
            merged_cont.append(left_cont[i])
            i += 1
        else:
            merged_cont.append(right_cont[j])
            j += 1

    merged_cont += left_cont[i:] + right_cont[j:]

    return merged_cont
