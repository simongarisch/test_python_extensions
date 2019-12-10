
cdef extern from "add.h":
    int pure_cadd(int a, int b)

# since cdef functions can't be used from python, we need to define a 'def' wrapper function
def cadd(int a, int b):
    return pure_cadd(a, b)
