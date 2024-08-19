# Checks

# Unknown variable in one line IF
# directory = sys.argv[1] if len(sys.argv) == 2 else "large"

list_1 = [1, 2, 3]

num = list_1[3] if len(list_1) > 1 else 90
print(num)
