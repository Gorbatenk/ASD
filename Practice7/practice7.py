from class_structure import StructureExample
from class_hamster import Hamster
from class_generator import Generator


class Sort(StructureExample):
    def sort(self):
        self._list.sort()

    def merge_sort(self):
        def merge(left, right):
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i].age <= right[j].age:  # Compare Hamsters based on age
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        if len(self._list) > 1:
            mid = len(self._list) // 2
            left_half = self._list[:mid]
            right_half = self._list[mid:]

            sort_left = Sort()
            sort_left._list = left_half
            sort_left.merge_sort()

            sort_right = Sort()
            sort_right._list = right_half
            sort_right.merge_sort()

            self._list = merge(sort_left._list, sort_right._list)

    def quicksort(self):
        def quick_sort_helper(arr, low, high):
            if low < high:
                pivot_index = partition(arr, low, high)
                quick_sort_helper(arr, low, pivot_index - 1)
                quick_sort_helper(arr, pivot_index + 1, high)

        def partition(arr, low, high):
            pivot = arr[low]
            i = low + 1
            j = high
            while True:
                while i <= j and arr[i].age <= pivot.age:  # Compare Hamsters based on age
                    i += 1
                while i <= j and arr[j].age > pivot.age:  # Compare Hamsters based on age
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                else:
                    break
            arr[low], arr[j] = arr[j], arr[low]
            return j

        quick_sort_helper(self._list, 0, len(self._list) - 1)


if __name__ == "__main__":
    gen = Generator()
    pl = [gen.generate_single() for _ in range(5)]
    print(pl)
    print('---')

    sort = Sort()
    sort.append(pl[0])
    sort.append(pl[1])
    sort.append(pl[2])
    sort.append(pl[3])
    sort.append(pl[4])
    for s in sort:
        print(s)

    print('---')
    sort.sort()
    print(sort[0])
    print(sort[1])
    print(sort[2])
    print(sort[3])
    print(sort[4])

    print('---')
    sort.merge_sort()
    print(sort[0])
    print(sort[1])
    print(sort[2])
    print(sort[3])
    print(sort[4])

    print('---')
    sort.quicksort()
    print(sort[0])
    print(sort[1])
    print(sort[2])
    print(sort[3])
    print(sort[4])

