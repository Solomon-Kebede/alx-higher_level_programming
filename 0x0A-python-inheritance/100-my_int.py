#!/usr/bin/python3

'''
Write a class `MyInt` that inherits from `int`:
    - `MyInt` is a rebel. `MyInt` has `==` and `!=` operators inverted
    - You are not allowed to import any module
'''


class MyInt(int):
	def __eq__(self, other):
		return str(self) != str(other)

	def __ne__(self, other):
		return str(self) == str(other)