#!/usr/bin/python3
"""Task 100 Project 0x0A Python"""


class MyInt(int):
    """"Class MyInt with int inherance"""
 
    def __eq__(self, __x: object) -> bool:
        return super().__ne__(__x)

    def __ne__(self, __x: object) -> bool:
        return super().__eq__(__x)
