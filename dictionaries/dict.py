band = {
    "vocals" : "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access all keys
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values)

# list of key/valur pairs as tuples
print(band.items())

# verify a key exists
print("guitar" in band)
print("triangle" in band)

# Change values
band["vocals"] = "coverdale"
band.update({"guitar": "JPJ"})

print(band)

# # Remove items
# print(band.pop("bass"))
# print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)

# Delate and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2