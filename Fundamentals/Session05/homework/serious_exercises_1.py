inventory = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"], 
}
print("Your inventory")
for key, vars in inventory.items():
    print(key, vars)

print("- " * 25)
print("Add key 'pocket'.")
inventory["pocket"] = ["seashell", "strange berry", "lint"]
print("Your inventory") 
for key, vars in inventory.items():
    print(key, vars)

print("- " * 25)
print("Remove 'dagger' under 'backpack' key.")
inventory["backpack"].remove("dagger")
print("Your inventory")
for key, vars in inventory.items():
    print(key, vars)

print("- " * 25)
print("Add 50 gold.")
inventory["gold"] = inventory["gold"] + 50
print("Your inventory")
for key, vars in inventory.items():
    print(key, vars)
