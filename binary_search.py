a = [1,2,3,4,55,76,8,9,565,1000,10]

a.sort()

def binary_search(arr, l, r, value):
  if r >= l:
    middle_index = l + (r - l) / 2
    middle = arr[middle_index]

    if middle == value:
      return middle_index
    elif middle < value:
      return binary_search(arr, middle_index + 1, r, value)
    else:
      return binary_search(arr, l, middle_index - 1, value)
  else:
    return -1


def iter_binary_search(arr, l, r, value):
  while l <= r:
    mid = l + (r - l) / 2
    middle = arr[mid]

    if middle == value:
      return mid
    elif middle < value:
      l = mid + 1
    else:
      r = mid - 1
  else:
    return -1


print(a)
print('8', binary_search(a, 0, len(a) - 1, 8))
print(565, binary_search(a, 0, len(a) - 1, 565))
print(1000, binary_search(a, 0, len(a) - 1, 1000))
print(9, binary_search(a, 0, len(a) - 1, 9))
print(5, binary_search(a, 0, len(a) - 1, 5))


print(a)
print('8', iter_binary_search(a, 0, len(a) - 1, 8))
print(565, iter_binary_search(a, 0, len(a) - 1, 565))
print(1000, iter_binary_search(a, 0, len(a) - 1, 1000))
print(9, iter_binary_search(a, 0, len(a) - 1, 9))
print(5, iter_binary_search(a, 0, len(a) - 1, 5))
