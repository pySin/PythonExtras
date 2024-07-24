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

for model in permutations:
    if model["Ivan"] == True and model["Kolio"] == True and model["rain"] == True \
            and model["Nikolai"] == False:
        print(f"Model found: {model}")


