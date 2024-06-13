#H24121133 統計一 陳星宇
f = int(input("Input the force: "))
m1 = int(input("Input the mass of m1: "))
d = int(input("Input the distance: "))
G = 6.67 * (10 ** (-11))
m2 = (f * (d ** 2)) / (G * m1)
print("The mass of m2 = ",m2)
e = m2 * (299792458 ** 2);
print("The energy of m2 = ",e)
