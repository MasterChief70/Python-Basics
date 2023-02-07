set1={11,22,33,44,55,66}
set2={11,22,33}
set3={11,55,99,20,30}
set4={6,7,8}
print(set1.intersection(set2))
print(set1.intersection(set3))
print(set1.intersection(set4))

print(set1.union(set2))
print(set1.union(set3))
print(set1.union(set4))

print(set1-set2)
print(set1-set3)
print(set1-set4)

print(set2-set1)

print(set1. issuperset(set2))
print(set1. issuperset(set3))
print(set1. issuperset(set4))

print(set2. issubset(set1))
print(set4. issubset(set2))
print(set4. issubset(set3))

print(set2.isdisjoint(set4))