def removeVowels(s):
    vowels = "aeiouAEIOU"
    sWithoutVowels = ""
    for eachChar in s:
        if eachChar not in vowels:
            sWithoutVowels = sWithoutVowels + eachChar
    return sWithoutVowels

x = removeVowels("compsci")

print(removeVowels("compsci"))
print(removeVowels("aAbEefIijOopUus"))
