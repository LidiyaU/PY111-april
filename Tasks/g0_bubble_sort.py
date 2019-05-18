# from typing import Sequence, TypeVar
#
# Tt = TypeVar("T")
#
#
# def sort(container: Sequence[_Tt]) -> Sequence[_Tt]:


def sort(container):
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    for a in range(len(container)-1, 0, -1):
        for i in range(a):
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]

    return container
