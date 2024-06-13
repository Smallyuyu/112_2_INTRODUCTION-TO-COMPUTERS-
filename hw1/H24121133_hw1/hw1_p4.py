#H24121133 統計一 陳星宇
h = int(input("Input the height of the 1st ball: "))
m1 = int(input("Input the mass of the 1st ball: "))
m2 = int(input("Input the mass of the 2nd ball: "))
E = m1 * 9.8 * h
v1 = (2 * E / m1) ** 0.5
print("The velocity of the 1st ball after slide: ","%.15f" % v1," m/s")
v2 = (2 * E / m2) ** 0.5
print("The velocity of the 2nd ball after collision: ","%.15f" % v2," m/s")