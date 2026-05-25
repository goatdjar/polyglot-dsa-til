from typing import TypeVar, Protocol

class Comparable(Protocol):
    def __lt__(self, other: any) -> bool: ...
    def __gt__(self, other: any) -> bool: ...
    def __eq__(self, other: any) -> bool: ...

T = TypeVar("T", bound=Comparable);

def binary_search(arr: list[T], target: T) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1
