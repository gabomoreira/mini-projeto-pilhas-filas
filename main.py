def eh_possivel_sair(lab):
    m = len(lab)
    n = len(lab[0])

    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n or lab[x][y] == '#' or visited[x][y]:
            return False

        visited[x][y] = True

        if x == m - 2 and y == n - 1:  
            return True

        return dfs(x + 1, y) or dfs(x - 1, y) or dfs(x, y + 1) or dfs(x, y - 1)

    visited = [[False] * n for _ in range(m)]
    return dfs(1, 0)

# Teste 1
labirinto1 = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', ' ', '#', ' ', ' ', '#', '#'],
    ['#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' '],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

resultado_esperado1 = True
resultado1 = eh_possivel_sair(labirinto1)
print(resultado1 == resultado_esperado1) 

# Teste 2
labirinto2 = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', '#'],
    ['#', ' ', ' ', '#', '#', '#', '#', ' ', '#', ' '],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

resultado_esperado2 = False
resultado2 = eh_possivel_sair(labirinto2)
print(resultado2 == resultado_esperado2) 
