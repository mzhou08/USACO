matrix = [1, 2, 3, 4]

print(matrix)

for char in input():
    if char == "H":
        matrix = [matrix[2], matrix[3], matrix[0], matrix[1]]
    if char == "V":
        matrix = [matrix[1], matrix[0], matrix[3], matrix[2]]

print(f"{matrix[0]} {matrix[1]} \n{matrix[2]} {matrix[3]}")


'''
LONG SOLUTION - F STRINGS DONT WORK
matrix=[[1,2], 
        [3,4]]

moves = []

def split(sequence):
    for move in sequence:
        moves.append(move)

split(input())

print(moves)

def HFlip(matrix):
    matrix[0] = matrix[0][::-1]
    print(matrix[0])
    matrix[1] = matrix[1][::-1]
    print(f"{matrix}")
    return matrix
    
def VFlip(matrix):
    temp = matrix[0]
    matrix[0] = matrix[1]
    matrix[1] = temp
    return matrix

for move in moves:
    if move == 'H':
        HFlip(matrix)
    if move == 'V':
        VFlip(matrix)
        

print(f'{matrix[0][0]} {matrix[0][1]}\n{matrix[1][0]} {matrix[1][1]}')
'''