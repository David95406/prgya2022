print("Addjon meg három számot! ")
a = int(input("$"))
b = int(input("$"))
c = int(input("$"))
szamok = []
szamok.append(a)
szamok.append(b)
szamok.append(c)
print("A legnagyobb szám: ", max(szamok))
print("A legkisebb szám: ", min(szamok))
szamok.remove(max(szamok))
szamok.remove(min(szamok))
print("A középső szám: ", szamok[0])