# Hashing using Separate Chaining, Linear Probing and Quadratic Probing

SIZE = 10


# ---------------- SEPARATE CHAINING ----------------
def separate_chaining(keys):
    table = [[] for _ in range(SIZE)]

    for key in keys:
        index = key % SIZE
        table[index].append(key)

    print("\nSeparate Chaining:")
    for i in range(SIZE):
        print(i, "->", table[i])


# ---------------- LINEAR PROBING ----------------
def linear_probing(keys):
    table = [None] * SIZE

    for key in keys:
        index = key % SIZE

        while table[index] is not None:
            index = (index + 1) % SIZE

        table[index] = key

    print("\nLinear Probing:")
    for i in range(SIZE):
        print(i, "->", table[i])


# ---------------- QUADRATIC PROBING ----------------
def quadratic_probing(keys):
    table = [None] * SIZE

    for key in keys:
        index = key % SIZE
        i = 0

        while table[(index + i * i) % SIZE] is not None:
            i += 1

        table[(index + i * i) % SIZE] = key

    print("\nQuadratic Probing:")
    for i in range(SIZE):
        print(i, "->", table[i])


# ---------------- MAIN ----------------
keys = [23, 43, 13, 27, 33, 53]

separate_chaining(keys)
linear_probing(keys)
quadratic_probing(keys)
