def rgb(r, g, b):
    #clamp = if n < 0: n = 0 elif n > 255: n = 255
    clamp = lambda n: max(min(255, n), 0)
    #format with 'X' param converts to hex e.g format(11, 'X') -> 'B'
    valToHex = lambda n: format(int(clamp(n) / 16), 'X') + format(int(clamp(n) % 16), 'X')
    return valToHex(r) + valToHex(g) + valToHex(b)