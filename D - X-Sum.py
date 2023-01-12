for test in range(int(input())):
    diag = {}
    anti = {}
    matrix = []
    
    for x in range(list(map(int , input().split()))[0]):
        matrix.append(list(map(int , input().split())))
    maxx = 0
    
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            dg = row + col
            ati = col - row
            diag[dg] = diag.get(dg , 0) + matrix[row][col]
            anti[ati] = anti.get(ati , 0) + matrix[row][col]
            
    maxx = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            dg = col + row
            at = col - row
            maxx = max(diag[dg] + anti[at] - matrix[row][col] , maxx)
    
    print(maxx)
