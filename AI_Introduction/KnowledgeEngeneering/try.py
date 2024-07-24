names = ["Ivan", "Kolio", "Nikolai", "rain"]
statuses = [True, False]

for i in range(len(names)):
    pairs = []
    for j in range(len(names)):
        pairs.append([names[j], True])
        pairs.append([names[j], False])
    print(pairs)
