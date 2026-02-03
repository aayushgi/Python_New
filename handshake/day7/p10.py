try:
    with open("lower.txt") as f1, open("upper.txt", "w") as f2:
        for line in f1:
            f2.write(line.upper())
except FileNotFoundError:
    print("Input file not found")