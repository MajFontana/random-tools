import os

DIR = r"C:\Program Files\Blender Foundation\"
EXT = ".py"
QUERY = "ANIM_animdata_get_context"

dirs = [DIR]
files = []
ext = EXT.lower()
match = []
q = bytes(QUERY, "utf-8")

print("Exploring %s ..." % DIR)
dcount = 0
while dirs:
    dcount += 1
    dr = dirs.pop(0)
    for i in os.listdir(dr):
        path = os.path.join(dr, i)
        if os.path.isfile(path):
            if i.lower().endswith(ext):
                files.append(path)
        else:
            dirs.append(path)
print("Found %i directories, %i target files." % (dcount, len(files)))

print("Searching ...")
for path in files:
    with open(path, "rb") as f:
        data = f.read()
    if q in data:
        match.append(path)
print("Finished, %i matching files found." % len(match))
for path in match:
    print("    %s" % path)
