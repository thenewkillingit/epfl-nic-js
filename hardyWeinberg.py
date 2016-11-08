#  Hardy-Weinberg Equalibrium in Python 3

#  Initialize Genotype frequencies

genotype1 = 0.15 
genotype2 = 0.35
genotype3 = 1 - (genotype1 + genotype2)
p = genotype1 + genotype2 / 2
q = 1 - p
# print("Generation 0:" + a1a1 + a1a2 + a2a2)


def create_next_generation():
    a1a1 = p * p
    a1a2 = 2 * p * q
    a2a2 = q * q
    i = 0
    print("Generation " + str(i) + ": " + str(genotype1) + str(genotype2) + str(genotype3))
    i += 1
    while i < 6:
        print("Generation " + str(i) + ": " + str(a1a1) + " " + str(a1a2) + " " + str(a2a2))
        i += 1


create_next_generation()
