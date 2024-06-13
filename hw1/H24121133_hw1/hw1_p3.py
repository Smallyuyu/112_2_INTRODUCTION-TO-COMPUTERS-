#H24121133 統計一 陳星宇
v = int(input("Input velocity: "))
pls = v / 299792458
print("Percentage of light speed = ",pls)
r = 1 / ((1 - (pls ** 2)) ** 0.5)
print("Travel time to Alpha Centauri = ","%.6f" % (4.3 / r))
print("Travel time to Barnard's Star = ","%.6f" % (6.0 / r))
print("Travel time to Betelgeuse (in the Milky Way) = ","%.6f" % (309 / r))
print("Travel time to Andromeda Galaxy (closest galaxy) = ","%.6f" % (2e6 / r))
