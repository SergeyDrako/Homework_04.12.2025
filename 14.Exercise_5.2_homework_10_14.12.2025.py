class Duration:
    def __init__(self, times):
        self.times = times


    def __add__(self, dad):
        return Duration( self.times + dad.times)

    def __str__(self):
        return f"{self.times} sec"

d1 = Duration(1.5)
d2 = Duration(2.7)
d3 = d1 + d2
print(d1)
print(d2)
print(d3)

# class Duration:
#     def __init__(self, seconds):
#         self.seconds = seconds
#
#     def __add__(self, other):
#         if isinstance(other, Duration):
#             return Duration(self.seconds + other.seconds)
#         return
#
#     def __str__(self):
#         return f"{self.seconds} sec"
#
# # Create Duration instances
# d1 = Duration(1.5)
# d2 = Duration(2.7)
# d3 = d1 + d2
# print(d1)
# # print(d2)
# # print(d3)



