def energy(m): # calcuate E = mc^2 when given m
    E = int(m)*300000000**2
    return int(E)

def main(): 
    mass = input("What is the mass?")
    print(energy(mass))

main()