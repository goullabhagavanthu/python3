users = ["Denver", "Kubrick", "Akira"]

data = ['Denver', 21, True]

emptylist = []

print("Denver" in emptylist)

print(users[0])
print(users[-2])

print(users.index('Akira'))

print(users[0:2])
print(users[1:])
print(users[-3: -1])

print(len(users))

users.append("Tarantino")
print(users)

users += ["David"]
print(users)

users.extend(["Coppola", "Tarkovsky"])
print(users)

users[2:2] = ["Nolan" , "Robert"]
print(users)

users.remove("Robert")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ['denver']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)


nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)


