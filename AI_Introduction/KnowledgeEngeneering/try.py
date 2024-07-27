# names = ["Ivan", "Kolio", "Nikolai", "rain"]
# statuses = [True, False]
#
# for i in range(len(names)):
#     pairs = []
#     for j in range(len(names)):
#         pairs.append([names[j], True])
#         pairs.append([names[j], False])
#     print(pairs)

# names_true = ["Ivan", True], ["Kolio", True], ["Nikolai", True], ["rain", True],
# names_false = ["Ivan", False], ["Kolio", False], ["Nikolai", False], ["rain", False]
#
# combinations = []
#
# for i in range(len(names_true)):
#     row = []
#     for j in range(len(names_false)):
#         inner_row = []
#         for q in range(len(names_true)):
#             if i == j:
#                 inner_row.append(names_true[q])
#             elif j == q:
#                 inner_row.append(names_false[q])
#             elif i == q:
#                 inner_row.append(names_false[q])
#             elif i != j:
#                 inner_row.append(names_true[q])
#         row.append(inner_row)
#     combinations.append(row)
#
#
# all_combinations = []
# for combs in combinations:
#     for comb in combs:
#         all_combinations.append(comb)
#
#
# print(len(combinations))
# print(len(all_combinations))
# print(all_combinations)

# true false combinations

models = []
for i in [True, True, True, True]:
    current_model = []
    for j in [False, False, False, False]:
        if i == j:
            current_model.append(i)
        else:
            current_model.append(j)
    models.append(current_model)

for m in models:
    print(m)

