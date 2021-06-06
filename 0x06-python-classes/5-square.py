#!/usr/bin/python3
"""empty
"""


class Square:
    """square size
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, v):
        if isinstance(v, int):
            if v < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = v
        else:
            raise TypeError("size must be an integer")
