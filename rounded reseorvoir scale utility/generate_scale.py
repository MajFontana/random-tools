import math

LENGTH = 2
WIDTH = 1.5
HEIGHT = 2
THICKNESS = 0.0025
STEP = 0.05

off = THICKNESS * 2
l = LENGTH - off
w = WIDTH - off
h = HEIGHT - off
r = w / 2

straight = h - w
box = straight * w * l
circle = math.pi * r ** 2
tube = circle * l
volume = box + tube
volreal = volume * 2

print("Total volume: %i L" % int(volreal * 1000))

ctrlow = r
ctrhigh = h - r
stage = 0
i = STEP
while i <= h:
    if stage == 0:
        level = 0
        top = 0
        if i >= ctrlow:
            bottom = r
            rect = i - ctrlow
            stage = 1
        else:
            bottom = i
            rect = 0
    elif stage == 1:
        level = tube / 2
        bottom = 0
        if i >= ctrhigh:
            rect = straight
            top = i - ctrhigh
            stage = 2
        else:
            top = 0
            rect = i - ctrlow
    elif stage == 2:
        bottom = 0
        rect = 0
        level = box + tube / 2
        top = i - ctrhigh
    
    level += rect * w * l

    a = r - bottom
    b = math.sqrt(r ** 2 - a ** 2)
    trisurf = a * b
    angle = math.acos(a / r) * 2
    sectsurf = (angle / (2 * math.pi)) * circle
    segment = sectsurf - trisurf
    level += segment * l

    a = top
    b = math.sqrt(r ** 2 - a ** 2)
    trisurf = a * b
    angle = math.acos(a / r) * 2
    sectsurf = (angle / (2 * math.pi)) * circle
    segment = sectsurf - trisurf
    level += (circle / 2 - segment) * l

    levreal = level * 2
    ratio = level / volume
    
    items = ("%i cm" % int(i * 100), "%i L" % int(levreal * 1000), "%i %%" % int(ratio * 100))
    print(" | ".join([item.center(10, " ") for item in items]))

    i += STEP
