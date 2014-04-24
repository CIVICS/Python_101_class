opposites = {"up": "down", "right": "wrong", "yes": "no"}
aliasedCopy = opposites

copy = opposites.copy()
#shallow copy

aliasedCopy["up"] = "potato"
#note you just changed both opposites and alised copy!
print(opposites)

#to chanage only one use the copyed one
copy["right"] = "rightMan!"
print(copy)

