class Colors:
    black = 0, 0, 0
    yellow = 255, 255, 000
    blue = 25, 83, 255
    white = 255, 255, 255
    red = 200, 0, 0
    green = 0, 200, 0
    bright_red = 255, 0, 0
    bright_green = 0, 255, 0

clamp = lambda x, minv,maxv: max(min(x, maxv), minv)
