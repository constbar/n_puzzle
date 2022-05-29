# import weakref

# class A(object):
#     instances = []
#     def __init__(self):
#         A.instances.append(weakref.ref(self))

# a, b, c = A(), A(), A()
# instances = [ref() for ref in A.instances if ref() is not None]

# print(instances)




# import gc

# class keki():
#     qwe = 123
#     qwe2 = 33
#     qwee = '1231231231231'
#     qqqqqqqq = {1: 123123}

#     def lol():
#         print()
#         pass

# k = keki()
# id_k = id(k)
# # id_k = 111111111111111
# # print('id_k', id_k)
# # print('type', type(id_k))
# import sys
# print(type(k))
# print('size', sys.getsizeof(k))

# # iiii = 0

# def objects_by_id(id_):
#     # iiii = iiii + 1

#     # print('len', len(gc.get_objects()))
#     # print('type', type(gc.get_objects()))
#     # print(gc.get_objects()[:10])
#     for obj in gc.get_objects():
#         if id(obj) == id_:
#             return obj
#     raise Exception("No found") # make not that id
# # print(iiii)
# print(objects_by_id(id_k))
# # print('res', objects_by_id(id_k).qwe)

# exit()
# import ctypes
# print(ctypes.cast(id_k, ctypes.py_object).value.qwe)
# # print(ctypes.cast(id_k, ctypes.py_object))


# # class Node:
# #     x = 2

# # c = Node()

# # d = Node()


# # print(id(c))
# # print(id(d))

from typing import Type, TypeVar

T = TypeVar('T')
S = TypeVar('S', bound=Shape)
class ndarray(Generic[T, S]):
    pass


a: ndarray  # just an array, shape and type are arbitrary
b: ndarray[float32, Any]  # array of floats with an unknown (dynamic) shape
c: ndarray[Any, Shape[100, 100]]  # array of dynamic types with fixed shape (100, 100)
c: ndarray[float32, Shape[100, 100]]
N = IntVar('N')
M = IntVar('M')
d: ndarray[float32, Shape[N, M]]