def swap_without_extraspace(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a

class Piece(Enum):
    EMPTY = 1,
    RED = 2,
    BLUE = 3

def find_winner(A):
    for x in A:
        for y in A:
            pass

    return Piece.BLUE
    
print(find_winner([[Piece.BLUE]]))
#print(swap_without_extraspace(9,4))