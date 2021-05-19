# Ход ладьи

lad_move = lambda a, b, c, d: f'Yes' if a == c or b == d else f'No'
print(lad_move(4, 4, 5, 4))

# Ход короля

king_move = lambda a, b, c, d: f'Yes' if abs(a - c) <= 1 and abs(b - d) <= 1 else f'No'
print(king_move(4, 4, 5, 5))

# Ход слона
elephant_move = lambda a, b, c, d: f'Yes' if (a - b == c - d) or (a + b == c + d) else f'No'
print(elephant_move(4, 4, 5, 5))


