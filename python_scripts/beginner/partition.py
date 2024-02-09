def is_even(num):
    return num % 2 == 0


# def partition(arr, fn):
#     even = []
#     odd = []
#     for num in arr:
#         if fn(num):
#             even.append(num)
#         else:
#             odd.append(num)
#     return [even, odd]



def partition(arr, fn):
    return [[num for num in arr if fn(num)], [num for num in arr if not fn(num)]]


print(partition([1,2,3,4], is_even)) # [[2,4],[1,3]]
print(partition([2,1,16,33,124,332,221,356,45,78], is_even))