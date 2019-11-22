
cdef extern from "add.h":
    int pure_cadd(int a, int b)


def py_pure_cadd(a, b):
    return pure_cadd(a, b)
