size = 5
for _ in range(size):
    print('\033[1A', end='')  # Remonte d'une ligne
    print('\033[0;30m' + '\u25A0' * size + '\033[0m', end='\n')  # Imprime la ligne