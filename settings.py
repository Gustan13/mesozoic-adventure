# 0 - rgb(255,255,255)
# 1 - rgb(0,0,0)

TILE_SIZE = 48
WIDTH, HEIGHT = TILE_SIZE * 16, TILE_SIZE * 16
FPS = 30

arrayMap = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1],
            [1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1],
            [1,2,0,0,0,0,1,1,1,1,0,0,0,0,2,1],
            [1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1],
            [1,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1],
            [1,0,1,2,0,1,0,1,1,0,1,0,2,1,0,1],
            [1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

# arrayMap = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
#             [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
#             [1,1,1,1,1,1,1,0,1,0,1,1,1,1,0,1],
#             [1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1],
#             [1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
#             [1,0,0,0,0,2,1,0,0,0,0,0,1,0,0,1],
#             [1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1],
#             [1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,1],
#             [1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,1],
#             [1,0,1,0,0,0,0,0,0,3,0,0,0,0,0,1],
#             [1,0,1,1,1,1,0,1,1,1,1,1,1,1,0,1],
#             [1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
#             [1,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1],
#             [1,0,1,0,1,0,1,0,1,1,0,1,1,1,1,1],
#             [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
#             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

# arrayMap = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
#             [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#             [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#             [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#             [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
#             [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
#             [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
#             [1, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#             [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# 0 - rgb(255,255,255)
# 1 - rgb(0,0,0)
