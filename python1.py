vocales=['a','e','i','o','u']
print(vocales)
for i in range (len(vocales)):
    print(f"{vocales[i]}")
for j in range (len(vocales)):
    print(f"Vocal: {vocales[j]}")
for f in range (len(vocales)):
    print(f"{vocales[f]}", end=",")
print()
for c in vocales:
    if c=="b":
        break
else:
    print("No ta")