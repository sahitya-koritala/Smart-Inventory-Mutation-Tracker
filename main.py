import copy

def create_inventory():
    return [
        {
            "item": "Laptop",
            "details": {
                "price": 50000,
                "stock": 10,
                "supplier": {"rating": 4.5}
            }
        },
        {
            "item": "Phone",
            "details": {
                "price": 20000,
                "stock": 25,
                "supplier": {"rating": 4.2}
            }
        }
    ]

def apply_discount(data, roll):
    index = roll % len(data)

    for i in range(len(data)):

        data[i]["details"]["price"] = int(data[i]["details"]["price"] * 0.9)

        if i == index:
            data[i]["details"]["stock"] -= 5

def compare_data(original, modified):
    changed = 0
    unchanged = 0

    for i in range(len(original)):
        if original[i]["details"] != modified[i]["details"]:
            changed += 1
        else:
            unchanged += 1

    return (changed, unchanged)

def show_diff(original, modified):
    for i in range(len(original)):
        if original[i]["details"] != modified[i]["details"]:
            print(original[i]["item"], "changed")
        else:
            print(original[i]["item"], "unchanged")

roll_number = int(input("Enter your roll number: "))

original = create_inventory()

shallow = original.copy()
apply_discount(shallow, roll_number)

original2 = create_inventory()
deep = copy.deepcopy(original2)
apply_discount(deep, roll_number)

print("\nOriginal (after shallow):")
print(original)

print("\nShallow Copy:")
print(shallow)

print("\nOriginal (for deep):")
print(original2)

print("\nDeep Copy:")
print(deep)

print("\nDifferences (Shallow):")
show_diff(original, shallow)

print("\nDifferences (Deep):")
show_diff(original2, deep)

print("\nSummary:")
print("Shallow:", compare_data(original, shallow))
print("Deep:", compare_data(original2, deep))

print("\nEvidence:")
print("Shallow shares same object:",
      original[0]["details"] is shallow[0]["details"])
print("Deep shares same object:",
      original2[0]["details"] is deep[0]["details"])
