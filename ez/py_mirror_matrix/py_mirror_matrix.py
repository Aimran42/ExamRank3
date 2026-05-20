def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [row[::-1] for row in matrix]

# dont push these test below

# out1 = mirror_matrix([[1, 2, 3], [4, 5, 6]])
# out2 = mirror_matrix([[1, 2], [3, 4], [5, 6]])
# out3 = mirror_matrix([[7]])
# out4 = mirror_matrix([[1, 2, 3, 4]])
# out5 = mirror_matrix([[-1, -2], [-3, -4]])


# print(out1)
# print(out2)
# print(out3)
# print(out4)
# print(out5)
