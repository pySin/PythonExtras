sentence = "If it rains Ivan will visit Kolio, otherwise Nikolai"

permutations = [{"Ivan": True, "Kolio": True, "Nikolai": True, "rain": True},
                {"Ivan": True, "Kolio": False, "Nikolai": True, "rain": True},
                {"Ivan": True, "Kolio": True, "Nikolai": False, "rain": True},
                {"Ivan": True, "Kolio": True, "Nikolai": True, "rain": False},
                {"Ivan": False, "Kolio": True, "Nikolai": True, "rain": True},

                {"Ivan": True, "Kolio": True, "Nikolai": False, "rain": False},
                {"Ivan": True, "Kolio": False, "Nikolai": False, "rain": True},
                {"Ivan": False, "Kolio": False, "Nikolai": True, "rain": True},
                {"Ivan": True, "Kolio": False, "Nikolai": True, "rain": False},
                {"Ivan": False, "Kolio": True, "Nikolai": False, "rain": True},
                {"Ivan": False, "Kolio": True, "Nikolai": True, "rain": False},

                {"Ivan": False, "Kolio": False, "Nikolai": False, "rain": False},
                {"Ivan": False, "Kolio": False, "Nikolai": False, "rain": True},
                {"Ivan": False, "Kolio": False, "Nikolai": True, "rain": False},
                {"Ivan": False, "Kolio": True, "Nikolai": False, "rain": False},
                {"Ivan": True, "Kolio": False, "Nikolai": False, "rain": False},
                ]

# "If it rains Ivan will visit Kolio, otherwise Nikolai"
for model in permutations:
    if model["Nikolai"] == True and not(model["Nikolai"] == True and model["rain"] == True):
        print(f"Model found: {model}")
        # The inability to visit Nikolai when it's raining and the fact that Nicolai
        # was visited implies that it doesn't rain. All the results that are returned
        # have value of false for "Rain"

