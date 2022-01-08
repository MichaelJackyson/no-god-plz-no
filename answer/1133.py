file_path = input()
with open(file_path, "r") as f:
    buf = f.read()

gun_names = buf.strip().split("\n")

pistol, smg, shotgun, ar, sniper = 0, 0, 0, 0, 0
for name in gun_names:
    if "PISTOL" in name:
        pistol += 1
    elif "SMG" in name:
        smg += 1
    elif "SHOTGUN" in name:
        shotgun += 1
    elif "AR" in name:
        ar += 1
    elif "SNIPER" in name:
        sniper += 1
    else:
        print("{} is an unknown type".format(name))

print("{} {} {} {} {}".format(pistol, smg, shotgun, ar, sniper))