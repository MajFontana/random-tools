from androidhelper import Android
import time
import os
import datetime
import math

def getDistance(dlat, dlon):
    unit = math.pi * 6371000 / 180
    y = dlat * unit
    x = dlon * unit * math.sin(dlat)
    return math.hypot(x, y)

drd = Android()

drd.wakeLockAcquirePartial()
drd.startLocating(100, 2)

os.system("clear")
print("Waiting for location data ...")
while 1:
    res = drd.readLocation().result
    if res:
        break
    time.sleep(0.1)

old = None
distance = 0
oldpos = None
start = None
maxspeed = 0
maxalt = 0
while 1:
    res = drd.readLocation().result
    if "gps" in res:
        loc = res["gps"]
    else:
        loc = res["network"]
    t = loc["time"]
    if t != old:
        old = t
        age = None
    else:
        sec = time.time() - (t / 1000)
        age = datetime.timedelta(seconds=sec)
    pos = (loc["latitude"], loc["longitude"])
    if oldpos:
        distance += getDistance(abs(pos[0] - oldpos[0]), abs(pos[1] - oldpos[1]))
    if not start:
        start = pos
        straight = 0
    else:
        straight = getDistance(abs(pos[0] - start[0]), abs(pos[1] - start[1]))
    oldpos = pos
    if loc["speed"] > maxspeed:
        maxspeed = loc["speed"]
    if loc["altitude"] > maxalt:
        maxalt = loc["altitude"]
    os.system("clear")
    print("Distance traveled: %.2f km" % (distance / 1000))
    print("Distance from start: %.2f km" % (straight / 1000))
    print()
    print("Altitude: %i m" % loc["altitude"])
    print("Speed: %i km/h" % int(loc["speed"] * 3.6))
    print("Bearing: %i °" % loc["bearing"])
    print()
    print("Max speed: %i km/h" % int(maxspeed * 3.6))
    print("Max altitude: %i m" % maxalt)
    print()
    print("Provider: %s" % loc["provider"])
    if age:
        minutes = age.seconds // 60
        seconds = age.seconds % 60
        if seconds >= 5:
                print("Location data old! (%i minutes %i seconds)" % (minutes, seconds))
    time.sleep(1)
