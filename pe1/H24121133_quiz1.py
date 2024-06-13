rsv = float(input("Please input a Richter scale value: "))
print("Richter scale value: ",rsv)
energy = 10 ** (1.5 * rsv + 4.8)
print("Equivalence in Joules: ","%.5f" % (energy))
tnt = 4.184e9
print("Equivalence in tons of TNT: ","%.5f" % (energy/tnt))
nl = 2930200
print("Equivalence in the number of nutritious lunches: ","%.5f" % (energy/nl))
