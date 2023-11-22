def main():
    mass = input("What is the mass?")
    print(energy(mass))

def energy(m):
    E = int(m)*300000000**2
    return int(E)

main()