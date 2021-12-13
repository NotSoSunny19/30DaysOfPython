it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Join A and B
A=A.union(B)
print(A)

# Find A intersection B
A=A.intersection(B)
print(A)

# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
A=A.union(B)
B = B.union(A)
print(A)
print(B)

# What is the symmetric difference between A and B
C = A.symmetric_difference(B)
print(C)

# Delete the sets completely
del A
del B
del it_companies
del age

print(A)
