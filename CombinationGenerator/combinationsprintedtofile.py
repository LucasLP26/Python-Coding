import itertools

def generate_combinations():
    digits = "0123456789"
    combinations = list(itertools.product(digits, repeat=4))
    return combinations

# Generate all combinations
all_combinations = generate_combinations()

# Write combinations to a file
with open("combinations.txt", "w") as file:
    for combination in all_combinations:
        file.write("".join(combination) + "\n")
