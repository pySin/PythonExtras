# Checks

# {1, 2, 3} = 1 # Not possible

# a = {1, 2, 3}
# print(a)

# Non declared variable

# def var_function():
#
#     x = False
#     if not x:
#         a = 0
#         x = True
#
#     a = a + 1

# --
# import random
#
# for j in range(20):
#     i = random.randrange(0, 8)
#     print(i, end=" ")

# props Syntax

# class Prop:
#
#     def __init__(self):
#         self.__var = None
#
#     @property
#     def var(self):
#         return self.var
#
#     @var.setter
#     def var(self, value):
#         self.var = value

# -- Add value to private set

# class Prop:
#
#     def __init__(self):
#         self.__var = set()
#
#     @property
#     def var(self):
#         return self.__var
#
#     # @var.setter
#     # def var(self, value):
#     #     self.var.add(value)
#
#
# p = Prop()
# p.var.add("Value1")
# p.var.add("Value2")
# print(p.var)

# --

