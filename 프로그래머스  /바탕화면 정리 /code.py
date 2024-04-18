def solution(wallpaper):
    n = len(wallpaper)
    m = len(wallpaper[0])
    
    lux = n
    luy = m
    rdx = 0
    rdy = 0
    
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == '#':
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i + 1)
                rdy = max(rdy, j + 1)
                
    return [lux, luy, rdx, rdy]
