rang = (20, 100)
div = 9
points = [(20, (0, 53, 255)), (30, (255, 255, 255)), (80, (255, 66, 0))]

if points[0][0] > rang[0]:
    points.insert(0, (rang[0], points[0][1]))
if points[-1][0] < rang[1]:
    points.append((rang[1], points[-1][1]))
step = (rang[1] - rang[0]) // (div - 1)
pts = [i[0] for i in points]
pos = 0
for x in range(rang[0], rang[1] + 1, step):
    while pos < len(pts) - 2 and pts[pos + 1] <= x:
        pos += 1
    sz = pts[pos + 1] - pts[pos]
    rps = x - pts[pos]
    prg = rps / sz
    col = [int(points[pos][1][i] * (1 - prg) + points[pos + 1][1][i] * prg) for i in range(3)]
    print(x, col)
